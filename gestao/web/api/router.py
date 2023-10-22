from fastapi.routing import APIRouter

from gestao.web.api import echo, monitoring, user

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
