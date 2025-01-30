import logging
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Any, Callable, Awaitable, Dict
from auth.database.json_driver.drivers import JSONConfigReader
from auth.schemas import User

logger = logging.getLogger(__name__)


class AdminAuthMiddleware(BaseMiddleware):
    def __init__(self, db_reader: JSONConfigReader) -> None:
        self.db_reader = db_reader

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message) and event.from_user:
            whitelisted_users: list[User] = self.db_reader.get_whitelisted_users()
            admin_ids: list[int] = [
                user.id for user in whitelisted_users if user.is_superuser
            ]

            if event.from_user.id in admin_ids:
                logger.info(
                    f"The user {event.from_user.id} is authorised to call admin commands"
                )
                return await handler(event, data)
            else:
                logger.info(
                    f"The user {event.from_user.id} is not authorised, ignoring the admin command"
                )
