from api.core import security
from fastapi import APIRouter, Depends
from . import document
api_router = APIRouter()
api_router.include_router(
    document.router, prefix="/document", tags=["document"], dependencies=[Depends(security.verify_http_auth_basic)]
)

