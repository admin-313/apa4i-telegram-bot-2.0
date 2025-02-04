import logging
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from typing import Any, Callable, Awaitable
from auth.database.json_driver.drivers import JSONConfigReader
from auth.schemas import User

logger = logging.getLogger(__name__)


class AuthMiddleware(BaseMiddleware):

    def __init__(self, db_reader: JSONConfigReader) -> None:
        self.db_reader = db_reader

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, (Message, CallbackQuery)) and event.from_user:
            whitelisted_users: list[User] = self.db_reader.get_whitelisted_users()
            request_user_id: int = event.from_user.id
            if request_user_id in [user.id for user in whitelisted_users]:
                logger.info(f"Request from id {request_user_id} has been accepted")
                return await handler(event, data)
            else:
                logger.info(f"Request from id {request_user_id} has been ignored")
