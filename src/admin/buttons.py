from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from admin.callbacks import AdminCallback

def get_paginator_first_page_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="▶️", callback_data=AdminCallback(action="next_page").pack())]]
    )


def get_paginator_last_page_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="◀️", callback_data=AdminCallback(action="previous_page").pack())]
        ]
    )


def get_paginator_default_page_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="◀️", callback_data=AdminCallback(action="previous_page").pack()),
                InlineKeyboardButton(text="▶️", callback_data=AdminCallback(action="next_page").pack()),
            ]
        ]
    )
