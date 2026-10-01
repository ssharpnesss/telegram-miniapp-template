from fastapi import Request, HTTPException
from aiogram.utils.web_app import WebAppInitData, safe_parse_webapp_init_data

from src.core.config import config

def auth(request: Request) -> WebAppInitData:
    try:
        auth_string = request.headers.get("Authorization")
        if auth_string and auth_string.startswith("tma"):
            data = safe_parse_webapp_init_data(
                config.BOT_TOKEN.get_secret_value(), auth_string[4:]
            )
            return data
        raise HTTPException(401, "Unathorized")
    except Exception:
        raise HTTPException(401, "Unathorized")