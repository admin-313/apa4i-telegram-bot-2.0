import os
from aiogram import Router
from aiogram.types.message import Message
from aiogram.filters.command import Command
from bot.buttons import get_main_menu_markup

LOGO_FILE_ID = os.getenv("LOGO_FILE_ID")

root_router = Router()



@root_router.message(Command("start"))
async def start_command(message: Message) -> None:
    if LOGO_FILE_ID:
        await message.answer_photo(
            photo=LOGO_FILE_ID,
            reply_markup=get_main_menu_markup()
        )