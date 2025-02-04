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
from auth.database.json_driver.drivers import JSONConfigWriter
from auth.schemas import User


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
        logger.debug(
            f"Sending /get responce as callback to message {message.message_id}"
        )
        return message
    else:
        if message.bot and message.from_user:
            logger.debug(
                f"Sending /get responce as message to user {message.from_user.id}"
            )
            return await message.bot.send_message(
                **response_text.as_kwargs(),
                chat_id=message.chat.id,
                reply_markup=buttons,
            )
        else:
            logger.error("Bot instance was not in Message")
            raise BotInstanceNotFound("Could not get bot out of the Message")


async def respond_to_remove(
    message: Message, db_writer: JSONConfigWriter, user_id: int
) -> Message:
    result: list[User] = db_writer.remove_whitelisted_user_by_id_if_exists(
        user_id=user_id
    )
    if result:
        reply_text: Text = Text("The user ", Code(user_id), " has been revoked")
        return await message.answer(**reply_text.as_kwargs())
    else:
        reply_text: Text = Text("The user ", Code(user_id), " is not in the database")
        return await message.answer(**reply_text.as_kwargs())

async def respond_to_promote(
    message: Message, db_writer: JSONConfigWriter, user_id: int
) -> Message:
    result: User | None = db_writer.promote_if_exists(user_id=user_id)
    if result:
        reply_text: Text = Text("The user ", Code(result.id), " has been promoted")
        return await message.answer(**reply_text.as_kwargs())
    else:
        reply_text: Text = Text("The user ", Code(user_id), " is either not in database or already promoted")
        return await message.answer(**reply_text.as_kwargs())