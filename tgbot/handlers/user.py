from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.keyboards.reply import menu_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
	await message.answer(f"Greetings, {message.from_user.full_name}, Welcome to the Tracker Bot!",
						 reply_markup=menu_keyboard())
