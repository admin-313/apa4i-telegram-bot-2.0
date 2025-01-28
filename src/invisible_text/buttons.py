from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from bot.callbacks import RootCallback


def get_invisible_text_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="❌Отмена", callback_data=RootCallback(action="root").pack()
                )
            ]
        ]
    )
