import logging
from datetime import datetime, timezone
from aiogram.filters.command import Command
from aiogram.types.message import Message
from aiogram import Router, F
from pydantic import ValidationError
from aiogram.utils.formatting import Code, Text
from admin.paginator.paginator import Paginator
from admin.paginator.schemas import PaginatorResponce
from auth.admin_auth_middleware import AdminAuthMiddleware
from auth.database.json_driver.drivers import JSONConfigReader, JSONConfigWriter
from auth.database.dispatcher import database_service_dispatcher
from auth.schemas import User

logger = logging.getLogger(__name__)

config_reader: JSONConfigReader = database_service_dispatcher["json_readonly"]()
config_writer: JSONConfigWriter = database_service_dispatcher[
    "json_admin_only_writer"
]()
admin_commands_router = Router(name=__name__)

admin_commands_router.message.middleware(
    AdminAuthMiddleware(db_reader=config_reader, db_writer=config_writer)
)


@admin_commands_router.message(F.text, Command("add", prefix="/"))
async def process_add_command(message: Message, db_writer: JSONConfigWriter) -> None:
    arguments: list[str] | None = message.text.split() if message.text else None
    caller_telegram_id: int | None = message.from_user.id if message.from_user else None

    if not arguments or not caller_telegram_id:
        return
    try:
        if len(arguments) > 1 and arguments[1].isdigit():
            user_id: int = int(arguments[1])
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
            await message.reply(**reply_text.as_kwargs())

        else:
            reply_text: Text = Text(
                "You have to provide user's id argument to perform this action! Example: \n",
                Code("/add 31457890"),
            )
            await message.reply(**reply_text.as_kwargs())
    except ValidationError as ve:
        logger.info(
            f"Argument validation error while adding User to the whitelist {str(ve)}"
        )
        await message.reply(text="Validation fail")


@admin_commands_router.message(F.text, Command("get", prefix="/"))
async def process_get_command(message: Message, db_reader: JSONConfigReader) -> None:
    arguments: list[str] | None = message.text.split() if message.text else None
    caller_telegram_id: int | None = message.from_user.id if message.from_user else None
    if not arguments or not caller_telegram_id:
        return
    
    paginator: Paginator = Paginator(elements_per_page=5, db_reader=db_reader)
    responce: PaginatorResponce = paginator.get_page(target_page=int(arguments[1]))
    await message.answer(text="".join([str(element.id) for element in responce.page_elements]))