import logging
from pydantic import ValidationError
from aiogram import Router, F
from datetime import datetime, timezone
from aiogram.filters.command import Command
from aiogram.types.message import Message
from aiogram.utils.formatting import Code, Text
from aiogram.types.callback_query import CallbackQuery
from admin.exceptions import MessageInstanceNotFound, UserInstanceNotFound, MessageIsEmpty
from admin.paginator.paginator import Paginator
from admin.utils import get_args_from_command
from admin.handlers import respond_to_get
from admin.callbacks import AdminCallback
from auth.admin_auth_middleware import AdminAuthMiddleware
from auth.database.json_driver.drivers import JSONConfigReader, JSONConfigWriter
from auth.database.dispatcher import database_service_dispatcher
from auth.schemas import User


logger = logging.getLogger(__name__)

config_reader: JSONConfigReader = database_service_dispatcher["json_readonly"]()
config_writer: JSONConfigWriter = database_service_dispatcher[
    "json_admin_only_writer"
]()
paginator: Paginator = Paginator(elements_per_page=10, db_reader=config_reader)
admin_commands_router = Router(name=__name__)

admin_auth_middleware = AdminAuthMiddleware(
    db_reader=config_reader, db_writer=config_writer, paginator=paginator
)
admin_commands_router.message.middleware(admin_auth_middleware)
admin_commands_router.callback_query.middleware(admin_auth_middleware)


@admin_commands_router.message(F.text, Command("add", prefix="/"))
async def process_add_command(message: Message, db_writer: JSONConfigWriter) -> Message:
    # Rewrite args parser for the get_args
    if not message.from_user:
        logger.error("Could not find caller's id")
        raise UserInstanceNotFound("Caller's telegram id doesn't appear to be there")
    
    if type(message) is not Message:
        logger.error("message type mismatch")
        raise MessageInstanceNotFound(
            f"The message type is not Message but {message.__class__.__name__}"
        )
    if not message.text:
        logger.error("The Message is empty")
        raise MessageIsEmpty("Message's text field can't be empty")

    arguments: list[str] = get_args_from_command(message.text)
    caller_telegram_id: int = message.from_user.id

    try:
        if arguments and arguments[0].isdigit():
            user_id: int = int(arguments[0])
            user = User(
                id=user_id,
                member_since=datetime.now(timezone.utc),
                is_superuser=False,
                last_known_name=None,
            )
            db_writer.add_whitelisted_user(user=user)

            logger.info(
                f"User {user_id} has been added to whitelist by admin {caller_telegram_id}"
            )
            reply_text: Text = Text(
                "The user ", Code(user_id), " has been successfully whitelisted"
            )
            return await message.reply(**reply_text.as_kwargs())

        else:
            reply_text: Text = Text(
                "You have to provide user's id argument to perform this action! Example: \n",
                Code("/add 31457890"),
            )
            return await message.reply(**reply_text.as_kwargs())
    except ValidationError as ve:
        logger.info(
            f"Argument validation error while adding User to the whitelist {str(ve)}"
        )
        await message.reply(text="Validation fail")


@admin_commands_router.message(F.text, Command("get", prefix="/"))
async def get_page_message(message: Message, paginator: Paginator) -> Message:
    if type(message) is Message and message.text:
        args_from_command: list[str] = get_args_from_command(command=message.text)
        page: int = (
            int(args_from_command[0])
            if args_from_command and args_from_command[0].isdecimal()
            else 1
        )

        return await respond_to_get(
            page=page, paginator=paginator, message=message, is_callback=False
        )
    else:
        logger.error("The message entity is blank")
        raise MessageInstanceNotFound("The message entity is blank")


@admin_commands_router.callback_query(AdminCallback.filter(F.action == "get_page"))
async def get_page_callback(
    callback: CallbackQuery, callback_data: AdminCallback, paginator: Paginator
) -> Message:
    message = callback.message
    if type(message) is Message and message.text:
        page: int = callback_data.target_page
        return await respond_to_get(
            page=page, message=message, paginator=paginator, is_callback=True
        )
    else:
        logger.error("The message entity is blank")
        raise MessageInstanceNotFound("The message entity is blank")
