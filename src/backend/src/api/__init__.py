from fastapi import APIRouter
from .routers.public import setup_public_routers
from .routers.v1 import setup_v1_routers

def setup_routers() -> APIRouter:
    router = APIRouter()

    router.include_router(setup_public_routers())
    router.include_router(setup_v1_routers(), prefix="/api")

    return router