from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from admin.callbacks import AdminCallback


def get_paginator_first_page_markup(next_target_page: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="▶️",
                    callback_data=AdminCallback(
                        action="next_page", target_page=next_target_page
                    ).pack(),
                )
            ]
        ]
    )


def get_paginator_last_page_markup(previous_target_page: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="◀️",
                    callback_data=AdminCallback(
                        action="previous_page", target_page=previous_target_page
                    ).pack(),
                )
            ]
        ]
    )


def get_paginator_default_page_markup(
    next_target_page: str, previous_target_page: str
) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="◀️",
                    callback_data=AdminCallback(
                        action="previous_page", target_page=previous_target_page
                    ).pack(),
                ),
                InlineKeyboardButton(
                    text="▶️",
                    callback_data=AdminCallback(
                        action="next_page", target_page=next_target_page
                    ).pack(),
                ),
            ]
        ]
    )
