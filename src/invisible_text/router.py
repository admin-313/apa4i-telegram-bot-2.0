from aiogram import F, Router
from aiogram.types.message import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import Code, Text
from invisible_text.callbacks import InvisibleTextCallback
from invisible_text.fsm_states import InvisibleTextForm
from invisible_text.buttons import (
    get_invisible_text_markup,
    get_invisible_text_on_success,
    get_invisible_text_on_repeat,
)
from invisible_text.service import get_unique_text
from admin.exceptions import MessageInstanceNotFound

invisible_text_router = Router()


@invisible_text_router.callback_query(
    InvisibleTextCallback.filter(F.action == "get_invisible_text")
)
async def invisible_text_callback(callback: CallbackQuery, state: FSMContext) -> Message:
    message = callback.message
    if type(message) is Message:
        await state.set_state(InvisibleTextForm.give_your_text)
        await message.edit_caption("Введите текст для преобразования:")
        await message.edit_reply_markup(reply_markup=get_invisible_text_markup())
        return message
    else:
        raise MessageInstanceNotFound("Could not find the message")


@invisible_text_router.callback_query(
    InvisibleTextCallback.filter(F.action == "repeat_get_invisible_text")
)
async def repeat_invisible_text_callback(
    callback: CallbackQuery, state: FSMContext
) -> Message:
    message = callback.message
    if type(message) is Message and message.text:
        await state.set_state(InvisibleTextForm.give_your_text)

        text_content = Text(Code(message.text), "\n\n", "Введите текст для преобразования")
        await message.edit_text(**text_content.as_kwargs())
        await message.edit_reply_markup(reply_markup=get_invisible_text_on_repeat())
        return message
    else:
        raise MessageInstanceNotFound("Could not find the message")


@invisible_text_router.message(InvisibleTextForm.give_your_text, F.text)
async def return_invisible_test(message: Message, state: FSMContext) -> Message:
    if message.text:
        text_content = Text(Code(get_unique_text(message.text)))
        await state.clear()
        return await message.reply(
            reply_markup=get_invisible_text_on_success(),
            **text_content.as_kwargs()
        )
    else:
        return await message.reply(text="Введите текст сообщением")
