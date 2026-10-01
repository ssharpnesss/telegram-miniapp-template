from typing import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise.contrib.fastapi import RegisterTortoise


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    from ..config import config, bot, dp, TORTOISE_ORM

    async with RegisterTortoise(app, config=TORTOISE_ORM):
        try:
            await bot.set_webhook(
                url=f"{config.API_URL}/webhook",
                drop_pending_updates=True,
                allowed_updates=dp.resolve_used_update_types()
            )
            yield
        finally:
            await bot.session.close()
