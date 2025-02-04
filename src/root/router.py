import os
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types.message import Message
from aiogram.filters.command import Command
from aiogram.types.callback_query import CallbackQuery
from root.buttons import get_main_menu_markup
from root.callbacks import RootCallback

LOGO_FILE_ID = os.getenv("LOGO_FILE_ID")

root_router = Router()


@root_router.message(Command("start"))
async def start_command(message: Message, state: FSMContext) -> None:
    # передача фото через Path
    if LOGO_FILE_ID and type(message) is Message:
        await state.clear()
        await message.answer_photo(
            photo=LOGO_FILE_ID,
            caption="Главное Меню",
            reply_markup=get_main_menu_markup(),
        )

@root_router.callback_query(RootCallback.filter(F.action == "new_root"))
async def send_new_root(query: CallbackQuery, state: FSMContext) -> None:
    if LOGO_FILE_ID and type(query.message) is Message:
        await state.clear()
        await query.message.answer_photo(
            photo=LOGO_FILE_ID,
            caption="Главное Меню",
            reply_markup=get_main_menu_markup(),
        )


@root_router.callback_query(RootCallback.filter(F.action == "root"))
async def root_callback(query: CallbackQuery, state: FSMContext) -> None:
    message = query.message
    if type(message) is Message:
        await state.clear()
        await message.edit_caption(caption="Главное Меню")
        if message.reply_markup:
            await message.edit_reply_markup(reply_markup=get_main_menu_markup())
