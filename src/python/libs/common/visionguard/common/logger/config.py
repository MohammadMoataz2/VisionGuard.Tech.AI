from pathlib import Path
from typing import Dict, Optional

from pydantic import AnyHttpUrl, BaseSettings, validator

# For more info SEE: https://pydantic-docs.helpmanual.io/usage/settings/


class Settings(BaseSettings):
    LOGGER_PREFIX: str = ""

    class Config:
        case_sensitive = True
