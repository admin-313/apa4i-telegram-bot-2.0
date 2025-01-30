import logging
from aiogram.filters.command import Command
from aiogram.types.message import Message
from aiogram import Router, F
from auth.admin_auth_middleware import AdminAuthMiddleware
from auth.database.json_driver.drivers import JSONConfigReader
from auth.database.dispatcher import database_service_dispatcher

logger = logging.getLogger(__name__)

config_reader: JSONConfigReader = database_service_dispatcher["json_readonly"]()
admin_commands_router = Router()
admin_commands_router.message.middleware(AdminAuthMiddleware(config_reader))


@admin_commands_router.message(F.text, Command("add", prefix="/"))
async def process_get_command(message: Message) -> None:
    logger.info("Process get command")
