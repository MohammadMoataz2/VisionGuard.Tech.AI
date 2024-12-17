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
import base64
import json
import requests

from fastapi import APIRouter, File, UploadFile
import base64
import requests

# Initialize the router and logger
router = APIRouter()
logger = logging.getLogger(settings.api_app_name)




def send_to_analyze(encoded_image, endpoint_port):
    # Convert image bytes to base64
    base64_encoded_image = base64.b64encode(encoded_image).decode('utf-8')

    # Create the payload in dataframe_split format
    payload = {
        "dataframe_split": {
            "columns": ["image_bytes"],
            "data": [[base64_encoded_image]]  # Use the base64 string instead of raw bytes
        }
    }

    # Send request to the MLflow model server
    response = requests.post(f"http://localhost:{endpoint_port}/invocations", json=payload)

    # Parse the response as JSON
    response_json = response.json()

    return response_json

@router.post("/face_detection")
async def face_detection(file: UploadFile = File(...)):
    # Read the file content as bytes
    image_bytes = await file.read()

    # Send the image bytes for analysis
    endpoint_port = 5002  # Adjust the port as necessary
    response_json = send_to_analyze(image_bytes, endpoint_port)

    # Return the response from the analysis
    return response_json

@router.post("/face_analyze")
async def face_analyze(file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Send the image bytes for analysis
    endpoint_port = 5001  # Adjust the port as necessary
    response_json = send_to_analyze(image_bytes, endpoint_port)

    # Return the response from the analysis
    return response_json
