from fastapi import APIRouter, Depends
from api.core import security
from . import healthcheck, face_analysis, adminstration

api_router = APIRouter()


api_router.include_router(
    face_analysis.router, prefix="/face_analysis", tags=["face_analysis"], dependencies=[Depends(security.verify_http_auth_basic)]
)
api_router.include_router(
    healthcheck.router, prefix="/health_check", tags=["health_check"],  dependencies=[Depends(security.verify_http_auth_basic)]
)
api_router.include_router(

    adminstration.router, prefix="/adminstration", tags=["adminstration"], dependencies=[Depends(security.verify_admin_http_auth_basic)]
)