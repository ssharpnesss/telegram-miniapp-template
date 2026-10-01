from typing import Any
from aiogram.types import Update

from src.api.core.base_service import ServiceResponse, BaseService
from src.core.config import bot, dp

class WebhookService(BaseService):
    async def bot_webhook_handler(self, body: Any) -> ServiceResponse:
        update = Update.model_validate(body, context={"bot": bot})
        await dp.feed_update(bot, update)

        return self.success({"ok": True})