import logging
import uuid
from typing import List
from uuid import UUID
from enum import Enum
from fastapi import Body
from fastapi import APIRouter, HTTPException
from api.core import settings
from api.db.models import Document
from api.api_interface.v1.schema import (
    SearchEngineUserAttribute,
    SearchEngineUserAttributeOther,
    SearchEngineQueryBs4Google,
    SearchEngineUserResultQuery,
    SearchEngineResultQuery,
    SearchEngineUserQuery,
)

# Initialize the router and logger
router = APIRouter()
logger = logging.getLogger(settings.api_app_name)

# Endpoint to create a new user
@router.post("/create_user")
async def create_user(
    user_name: str,
    user_password: str,
    user_email: str,
    user_attributes: SearchEngineUserAttribute,
    user_attributes_other: SearchEngineUserAttributeOther,
):
    """
    Create a new user in the database with the provided attributes.

    Args:
        user_name (str): Name of the user.
        user_password (str): Password of the user.
        user_email (str): Email of the user.
        user_attributes (SearchEngineUserAttribute): User attributes.
        user_attributes_other (SearchEngineUserAttributeOther): Additional user attributes.

    Returns:
        Document: The created user document or a message indicating the email is already in use.
    """
    # Check if the email already exists in the database
    existing_user = await Document.find_one(Document.user_email == user_email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already in use")

    # Create a new user document
    user_obj = Document(
        user_name=user_name,
        user_password=user_password,
        user_email=user_email,
        user_attributes=user_attributes,
        user_attributes_other=user_attributes_other,
    )

    # Insert the new user into the database
    await user_obj.insert()
    logger.info(f"New user created: {user_obj}")

    return {"message": "User created successfully", "user": user_obj}



# Endpoint to submit a search query
@router.post("/submit_query")
async def submit_query(
    query: str = "",
    id: str = "",
):
    """
    Submit a search query for a specific user and store the results.

    Args:
        query (str): The search query string.
        id (str): The UUID of the user.

    Returns:
        dict: A message and the query result.
    """
    # Fetch the user object from the database using the UUID
    try:
        user_id = UUID(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    user_obj = await Document.find_one(Document.user_id == user_id)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    logger.info(f"Fetched user: {user_obj}")

    # Perform the search using the query
    search_result = SearchEngineQueryBs4Google(SEARCH_TERM=query)
    logger.info(f"Search result generated: {search_result}")

    # Create a query result object
    user_query_result = SearchEngineUserResultQuery(
        user_query=SearchEngineUserQuery(query_obj=search_result),
        result_query=SearchEngineResultQuery(query_result=search_result.search()),
    )
    logger.info(f"User query result created: {user_query_result}")

    # Add the result to the user's document
    if not hasattr(user_obj, "user_query_result"):
        user_obj.user_query_result = []

    user_obj.user_query_result.append(user_query_result)

    # Save the updated document
    await user_obj.save()

    return {"message": "Query submitted successfully", "result": user_query_result}







# Enum to specify the field to update
class UpdateField(str, Enum):
    username = "username"
    email = "email"

# Endpoint to update either the username or email
@router.put("/update_user_field")
async def update_user_field(
    id: str,
    current_password: str,
    field_to_update: UpdateField = UpdateField.username,
    new_value: str = "",
):
    """
    Update either the user's username or email if the provided password and ID are valid.

    Args:
        id (str): The UUID of the user.
        current_password (str): The current password of the user.
        field_to_update (UpdateField): The field to update ('username' or 'email').
        new_value (str): The new value for the specified field.

    Returns:
        dict: A success message if the update is successful.
    """
    # Validate the UUID
    try:
        user_id = UUID(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Find the user in the database
    user_obj = await Document.find_one(Document.user_id == user_id)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if user_obj.user_password != current_password:
        raise HTTPException(status_code=401, detail="Invalid password")

    # Update the specified field
    if field_to_update == UpdateField.username:
        user_obj.user_name = new_value
        logger.info(f"User ID {user_id} updated username to {new_value}")
    elif field_to_update == UpdateField.email:
        # Check if the email is already in use
        existing_user = await Document.find_one(Document.user_email == new_value)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email is already in use")
        user_obj.user_email = new_value
        logger.info(f"User ID {user_id} updated email to {new_value}")

    # Save the updated user document
    await user_obj.save()

    return {"message": f"User {field_to_update} updated successfully", "new_value": new_value}



@router.put("/update_password")
async def update_password(
    id: str,
    current_password: str,
    new_password: str = Body(..., description="The new password for the user"),
):
    """
    Update the user's password if the current password and user ID are valid.

    Args:
        id (str): The UUID of the user.
        current_password (str): The current password of the user.
        new_password (str): The new password to set.

    Returns:
        dict: A success message if the update is successful.
    """
    # Validate the UUID
    try:
        user_id = UUID(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Find the user in the database
    user_obj = await Document.find_one(Document.user_id == user_id)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if user_obj.user_password != current_password:
        raise HTTPException(status_code=401, detail="Invalid current password")

    # Update the user's password
    user_obj.user_password = new_password
    logger.info(f"User ID {user_id} updated their password")

    # Save the updated user document
    await user_obj.save()

    return {"message": "Password updated successfully"}


@router.delete("/delete_user")
async def delete_user(
    id: str,
    current_password: str,
):
    """
    Delete a user from the database if the provided ID and current password are valid.

    Args:
        id (str): The UUID of the user.
        current_password (str): The current password of the user.

    Returns:
        dict: A success message if the user is successfully deleted.
    """
    # Validate the UUID
    try:
        user_id = UUID(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Find the user in the database
    user_obj = await Document.find_one(Document.user_id == user_id)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if user_obj.user_password != current_password:
        raise HTTPException(status_code=401, detail="Invalid password")

    # Delete the user
    await user_obj.delete()
    logger.info(f"User ID {user_id} deleted successfully")

    return {"message": "User deleted successfully"}
