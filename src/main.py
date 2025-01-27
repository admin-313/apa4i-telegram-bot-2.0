import os
import logging
import asyncio
from pydantic import ValidationError
from exceptions import ConfigurationException
from schemas import BotConfiguration


async def main() -> None:
    logging.basicConfig(
        format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
    )
    logger = logging.getLogger(__name__)

    try:
        # Pylance ignore. The purpouse of this string is to check whether
        # the config_data contains correct values
        config = BotConfiguration(
            link_to_fb_parser=os.getenv("LINK_TO_FB_PARSER"), # type: ignore
            admin_telegram_id=os.getenv("ADMIN_TELEGRAM_ID"), # type: ignore
            bot_token=os.getenv("BOT_TOKEN"), # type: ignore
        )  # type: ignore

    except ValidationError as ve:
        logger.critical(f"Could not load configurational variables: {str(ve)}")
        raise ConfigurationException("Have you defined all env variables needed?")


if __name__ == "__main__":
    asyncio.run(main())
