from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from invisible_text.callbacks import InvisibleTextCallback


def get_main_menu_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Проверка Доменов", callback_data="domain_check"
                ),
                InlineKeyboardButton(
                    text="Уникализация Медиа", callback_data="unique_media"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Пошарка Пикселя", callback_data="pixel_sharing"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Невидимый Текст",
                    callback_data=InvisibleTextCallback(
                        action="get_invisible_text"
                    ).pack(),
                )
            ],
        ]
    )
