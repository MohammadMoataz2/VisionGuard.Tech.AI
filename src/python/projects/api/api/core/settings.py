import os
import secrets
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "visionguard.tech.ai.api"
    app_version: str = "0.0.1"
    auth_username: str = "Foo"
    auth_password: str = "Bar"

    auth_admin_username: str = "Bar"
    auth_admin_password: str = "Baz"
    USE_DOC_AUTH: bool = True

    API_V1_STR: str = "/api/v1"

    APP_DEBUG: str = True


    DB_CONN_STRING: str
    DB_NAME: str = "dev"
    DB_MAX_CONNECTIONS: int = 10
    DB_MIN_CONNECTIONS: int = 10
    DB_INIT_DURING_STARTUP: bool = True


    class Config:
        case_sensitive = True



settings = Settings(_env_file=os.getenv("APP_DOTENV_PATH"))
if settings.APP_DEBUG:
    from pprint import pprint

    pprint(settings.dict())