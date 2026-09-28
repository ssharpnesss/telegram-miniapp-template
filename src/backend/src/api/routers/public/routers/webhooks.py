from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.api.routers.public.services import WebhookService

router = APIRouter()
service = WebhookService()

@router.post("/webhook")
async def telegram_webhook_handler(request: Request) -> JSONResponse:
    res = await service.bot_webhook_handler(await request.json())
    return JSONResponse(**res.response())