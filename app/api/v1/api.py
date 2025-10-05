from fastapi import APIRouter
from .routers import dumb_router

api_v1_router = APIRouter()

api_v1_router.include_router(router=dumb_router, prefix="/dumbs", tags=["Dumbs"])
