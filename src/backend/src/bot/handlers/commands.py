from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram import types

from src.db.models import User
from src.bot.keyboards.builder import start_markup

router = Router()

@router.message(CommandStart())
async def cmd_start_handler(message: types.Message):
    user = await User.filter(user_id=message.from_user.id).exists()
    if not user:
        await User.create(
            user_id=message.from_user.id,
            name=message.from_user.first_name,
            username=message.from_user.username
        )
    await message.answer("Welcome ту zachetk.site !", reply_markup=start_markup())