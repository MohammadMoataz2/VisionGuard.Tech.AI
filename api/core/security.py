import secrets
from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from jose import JWTError, jwt

from .settings import settings

security = HTTPBasic()


def verify_http_auth_basic(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, settings.auth_username)
    correct_password = secrets.compare_digest(credentials.password, settings.auth_password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def verify_admin_http_auth_basic(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, settings.auth_admin_username)
    correct_password = secrets.compare_digest(credentials.password, settings.auth_admin_password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username