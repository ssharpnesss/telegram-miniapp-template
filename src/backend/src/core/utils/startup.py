from typing import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.context import TortoiseContext


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    from ..config import config, bot, dp, TORTOISE_ORM

    await bot.set_webhook(
        url=f"{config.API_URL}/webhook",
        drop_pending_updates=True,
        allowed_updates=dp.resolve_used_update_types()
    )
    await Tortoise.init(TORTOISE_ORM)
    yield
    await bot.session.close()
    await Tortoise.close_connections()