from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Any, Callable, Awaitable

class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any]
    ) -> Any:
        pass