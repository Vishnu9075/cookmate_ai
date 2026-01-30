from fastapi import APIRouter
from .health import router as health_router
from .compile import router as compile_router
from .sessions import router as sessions_router
from .commands import router as commands_router

api_router = APIRouter
api_router.include_router(health_router)
api_router.include_router(compile_router, prefix="/compile",tags=["compile"])
api_router.include_router(sessions_router, prefix="/sessions", tags=["sessions"])
api_router.include_router(commands_router, prefix="/sessions", tags=["commands"])