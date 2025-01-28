import os
from aiogram import Router, F
from aiogram.types.message import Message
from aiogram.filters.command import Command
from aiogram.types.callback_query import CallbackQuery
from bot.buttons import get_main_menu_markup
from bot.callbacks import RootCallback

LOGO_FILE_ID = os.getenv("LOGO_FILE_ID")

root_router = Router()


@root_router.message(Command("start"))
async def start_command(message: Message) -> None:
    if LOGO_FILE_ID:
        await message.answer_photo(
            photo=LOGO_FILE_ID,
            caption="Главное Меню",
            reply_markup=get_main_menu_markup(),
        )


@root_router.callback_query(RootCallback.filter(F.action == "root"))
async def root_callback(callback: CallbackQuery) -> None:
    message = callback.message
    if type(message) is Message:
        await message.edit_caption(caption="Главное Меню")
        if message.reply_markup:
            await callback.message.edit_reply_markup(reply_markup=get_main_menu_markup())  # type: ignore
