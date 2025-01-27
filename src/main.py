import logging
import asyncio
from aiogram import Bot
from bot.bot import get_dispatcher
from config.config import get_bot_configuration

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    bot_config = get_bot_configuration()
    dp = get_dispatcher()
    bot = Bot(bot_config.bot_token)
    await dp.start_polling(bot)  # type: ignore


if __name__ == "__main__":
    asyncio.run(main())
