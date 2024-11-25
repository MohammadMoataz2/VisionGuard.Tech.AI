import logging
import random
import tempfile
import uuid
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path as FSPath
from pydoc import describe
from typing import List, Optional, Union
from uuid import uuid4


from api.db.models import Document
from fastapi import APIRouter, Depends
from api.core import settings

router = APIRouter()

logger = logging.getLogger(settings.app_name)

from visionguard.common.api_interface.v1.schema import (
    SearchEngineUserAttributeOther, SearchEngineUserAttribute, SearchEngineUser, SearchEngineQueryBs4Google,
SearchEngineUserResultQuery, SearchEngineResultQuery, SearchEngineUserQuery)


@router.post("/create_user")
async def create_user(
    user_name: str,
    user_password: str,
    user_email: str,
    user_attributes: SearchEngineUserAttribute,
    user_attributes_other: SearchEngineUserAttributeOther
):
    print(user_name)
    print(user_password)
    print(user_email)
    # Create SearchEngineUser instance with provided attributes

    user_obj = Document(
        user_name=user_name,
        user_password=user_password,
        user_email=user_email,
        user_attributes=user_attributes,
        user_attributes_other=user_attributes_other
    )
    print(user_obj)

    await user_obj.insert()

    return user_obj


from fastapi import HTTPException
from uuid import UUID
from api.db.models import Document
from beanie import PydanticObjectId


@router.post("/submit_query")
async def submit_query(
        query: str,
        id: str,
):
    # Fetch the user object from the database using the ID
    user_obj = await Document.find_one(Document.user_id == UUID(id))

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    print("user_obj", user_obj)

    # Perform the search using the query
    search_result = SearchEngineQueryBs4Google(SEARCH_TERM = query)

    # Append the query result to the user object
    print("search_result",search_result)
    user_query_result = SearchEngineUserResultQuery(
        user_query=SearchEngineUserQuery(query_obj=search_result),
        result_query=SearchEngineResultQuery(query_result=search_result.search()),
    )
    print("user_query_result",user_query_result)

    # Add the result to the user's document (you may need a list attribute for results)
    if not hasattr(user_obj, "user_query_result"):
        user_obj.user_query_result = []

    user_obj.user_query_result.append(user_query_result)

    # Save the updated document
    await user_obj.save()

    return {"message": "Query submitted successfully", "result": user_query_result}
