from fastapi import APIRouter
from backend.app.api.routes import auth, data

api_router = APIRouter()

api_router.include_router(auth.auth_router, prefix="/auth")
api_router.include_router(data.data_router, prefix="/data")