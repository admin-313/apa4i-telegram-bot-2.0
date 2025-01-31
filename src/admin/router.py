import logging
from aiogram.filters.command import Command
from aiogram.types.message import Message
from aiogram import Router, F
from auth.admin_auth_middleware import AdminAuthMiddleware
from auth.database.json_driver.drivers import JSONConfigReader, JSONConfigWriter
from auth.database.dispatcher import database_service_dispatcher

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
async def process_get_command(message: Message, db_writer: JSONConfigWriter) -> None:
    logger.info("Process get command")
    await message.answer(
        text="".join(str(user.id) for user in db_writer.get_whitelisted_users())
    )
