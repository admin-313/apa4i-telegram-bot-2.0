from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Any, Callable, Awaitable
from auth.database.json_driver.drivers import JSONConfigReader
from auth.schemas import User


class AuthMiddleware(BaseMiddleware):

    def __init__(self, json_reader: JSONConfigReader) -> None:
        self.json_reader = json_reader

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, Message) and event.from_user:
            whitelisted_users: list[User] = self.json_reader.get_whitelisted_users()
            if event.from_user.id in [user.id for user in whitelisted_users]:
                return await handler(event, data)
