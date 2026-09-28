from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.core.config import config

def start_markup():
    builder = InlineKeyboardBuilder()

    builder.button(text="Открыть Zachetk", web_app=WebAppInfo(url=config.MINIAPP_URL))
    return builder.as_markup()