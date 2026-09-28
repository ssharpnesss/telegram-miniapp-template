from fastapi import APIRouter
from .routers import webhooks

def setup_public_routers() -> APIRouter:
    router = APIRouter()

    router.include_router(webhooks.router)

    return router