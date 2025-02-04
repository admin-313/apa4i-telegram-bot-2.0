import logging
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from typing import Any, Callable, Awaitable
from admin.paginator.paginator import Paginator
from auth.database.json_driver.drivers import JSONConfigReader, JSONConfigWriter
from auth.schemas import User

logger = logging.getLogger(__name__)


class AdminAuthMiddleware(BaseMiddleware):
    def __init__(
        self,
        db_reader: JSONConfigReader,
        db_writer: JSONConfigWriter,
        paginator: Paginator,
    ) -> None:
        self.db_reader = db_reader
        self.db_writer = db_writer
        self.paginator = paginator

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, (Message, CallbackQuery)) and event.from_user:
            whitelisted_users: list[User] = self.db_reader.get_whitelisted_users()
            admin_ids: list[int] = [
                user.id for user in whitelisted_users if user.is_superuser
            ]

            if event.from_user.id in admin_ids:
                logger.info(
                    f"The user {event.from_user.id} is authorised to call admin commands"
                )

                data["db_writer"] = self.db_writer
                data["db_reader"] = self.db_reader
                data["paginator"] = self.paginator
                return await handler(event, data)
            else:
                logger.info(
                    f"The user {event.from_user.id} is not authorised, ignoring the admin command"
                )
