import asyncio
from aiogram import Bot
from bot.bot import get_dispatcher
from config.config import get_bot_configuration


async def main() -> None:
    bot_config = get_bot_configuration()
    dp = get_dispatcher()
    bot = Bot(bot_config.bot_token)
    await dp.start_polling(bot) # type: ignore


if __name__ == "__main__":
    asyncio.run(main())
