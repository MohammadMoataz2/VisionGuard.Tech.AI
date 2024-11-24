import logging
import random
import tempfile
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path as FSPath
from pydoc import describe
from typing import List, Optional, Union



from api.db.models import Document
from fastapi import APIRouter, Depends
from api.core import settings

router = APIRouter()

logger = logging.getLogger(settings.app_name)

from visionguard.common.api_interface.v1.schema.search_engine_user import SearchEngineUserAttributeOther, SearchEngineUserAttribute, SearchEngineUser


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

    await user_obj.insert()

    return user_obj

