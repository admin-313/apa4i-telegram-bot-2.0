import logging
from aiogram.types.message import Message
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.formatting import Code, Text
from admin.exceptions import BotInstanceNotFound
from admin.paginator.paginator import Paginator
from admin.paginator.schemas import PaginatorResponse
from admin.buttons import (
    get_paginator_default_page_markup,
    get_paginator_last_page_markup,
    get_paginator_first_page_markup,
)


logger = logging.getLogger(__name__)


async def respond_to_get(
    message: Message, paginator: Paginator, page: int, is_callback: bool
) -> Message:
    response: PaginatorResponse = paginator.get_page(page)
    response_text: Text = Text(
        f"Page {response.current_page} of {response.total_pages}\n",
        *(Code(str(user.id) + "\n") for user in response.page_elements),
    )
    buttons: InlineKeyboardMarkup | None = None

    if response.current_page != response.total_pages and response.current_page != 1:
        buttons = get_paginator_default_page_markup(
            next_target_page=response.current_page + 1,
            previous_target_page=response.current_page - 1,
        )
    elif response.current_page == response.total_pages:
        buttons = get_paginator_last_page_markup(
            previous_target_page=response.current_page - 1
        )
    elif response.current_page == 1:
        buttons = get_paginator_first_page_markup(
            next_target_page=response.current_page + 1
        )

    if is_callback:
        await message.edit_text(**response_text.as_kwargs())
        await message.edit_reply_markup(reply_markup=buttons)
        logger.debug(f"Sending /get responce as callback to message {message.message_id}")
        return message
    else:
        if message.bot and message.from_user:
            logger.debug(f"Sending /get responce as message to user {message.from_user.id}")
            return await message.bot.send_message(
                **response_text.as_kwargs(),
                chat_id=message.chat.id,
                reply_markup=buttons,
            )
        else:
            logger.error("Bot instance was not in Message")
            raise BotInstanceNotFound("Could not get bot out of the Message")