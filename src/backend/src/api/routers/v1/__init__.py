from src.api.core.auth import auth
from fastapi import APIRouter, Depends
from .routers import user

def setup_v1_routers() -> APIRouter:
    router = APIRouter(prefix="/v1", dependencies=[Depends(auth)])

    router.include_router(user.router)

    return router