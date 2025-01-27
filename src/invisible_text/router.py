from aiogram import F, Router
from aiogram.types.message import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.context import FSMContext
from invisible_text.callbacks import InvisibleTextCallback
from invisible_text.form import Form
from invisible_text.buttons import get_invisible_text_markup
from invisible_text.service import get_unique_text

invisible_text_router = Router()


@invisible_text_router.callback_query(
    InvisibleTextCallback.filter(F.action == "get_invisible_text")
)
async def invisible_text_callback(
    query: CallbackQuery, callback_data: InvisibleTextCallback, state: FSMContext
) -> None:
    await state.set_state(Form.get_unique_text)
    await query.message.edit_caption("Введите текст для преобразования:")  # type: ignore
    await query.message.edit_reply_markup(reply_markup=get_invisible_text_markup())  # type: ignore


@invisible_text_router.message(Form.text_accepted)
async def return_invisible_test(message: Message, state: FSMContext) -> None:
    await state.clear()
    if message.text:
        await message.reply(get_unique_text(message.text))
