from typing import Annotated
from aiogram.utils.web_app import WebAppInitData
from src.api.core.auth import auth
from fastapi import Depends

AuthData =  Annotated[WebAppInitData, Depends(auth)]