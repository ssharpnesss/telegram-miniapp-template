from src.api.core.dependencies import AuthData
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.api.routers.v1.services import UserService

router = APIRouter(prefix="/users")
service = UserService()

@router.get("/me")
async def get_me(auth_data: AuthData) -> JSONResponse:
    res = await service.get_me(auth_data)
    return JSONResponse(**res.response())