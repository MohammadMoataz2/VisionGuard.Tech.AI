from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    app_name: str = "sanadcash.expenseai.datarepo"
    app_version: str = "0.0.1"
    auth_username: str = "Foo"
    auth_password: str = "Bar"
    auth_admin_username: str = "Bar"
    auth_admin_password: str = "Baz"
    USE_DOC_AUTH: bool = True
    API_V1_STR: str = "/api/v1"
    APP_DEBUG: bool = True
    DB_MAX_CONNECTIONS: int = 10
    DB_MIN_CONNECTIONS: int = 10
    DB_INIT_DURING_STARTUP: bool = True

    LOGGER_PREFIX: str = ""


settings = Settings()

if settings.APP_DEBUG:
    from pprint import pprint
    pprint(settings.dict())