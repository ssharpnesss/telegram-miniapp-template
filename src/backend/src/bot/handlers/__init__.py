from aiogram import Router
from . import commands

def setup_user_handlers() -> Router:
    router = Router()

    router.include_router(commands.router)
    return router