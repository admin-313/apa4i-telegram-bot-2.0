from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


def get_paginator_first_page_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="▶️", callback_data="next_page")]]
    )


def get_paginator_last_page_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="◀️", callback_data="previous_page")]
        ]
    )


def get_paginator_default_page_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="▶️", callback_data="next_page"),
                InlineKeyboardButton(text="◀️", callback_data="previous_page"),
            ]
        ]
    )
