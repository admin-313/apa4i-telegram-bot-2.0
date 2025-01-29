from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Any, Callable, Awaitable
from src.auth.database.service import JSONConfigReader


class AuthMiddleware(BaseMiddleware):

    def __init__(self, json_reader: JSONConfigReader) -> None:
        self.json_reader = json_reader

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        pass
