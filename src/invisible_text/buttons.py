from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from root.callbacks import RootCallback
from invisible_text.callbacks import InvisibleTextCallback


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


def get_invisible_text_on_repeat() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="❌Отмена",
                    callback_data=RootCallback(action="new_root").pack(),
                )
            ]
        ]
    )


def get_invisible_text_on_success() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔄Повторить",
                    callback_data=InvisibleTextCallback(
                        action="repeat_get_invisible_text"
                    ).pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️Назад", callback_data=RootCallback(action="new_root").pack()
                )
            ],
        ]
    )
