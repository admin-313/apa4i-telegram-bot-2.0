import os
import logging
from pydantic import ValidationError
from main.exceptions import ConfigurationException
from main.schemas import BotConfiguration

logger = logging.getLogger(__name__)

async def main() -> None:

    try:
        config = BotConfiguration(
            link_to_fb_parser=os.getenv("LINK_TO_FB_PARSER"), # type: ignore
            admin_telegram_id=os.getenv("ADMIN_TELEGRAM_ID"), # type: ignore
            bot_token=os.getenv("BOT_TOKEN"), # type: ignore
        )

    except ValidationError as ve:
        logger.critical(f"Could not load configurational variables: {str(ve)}")
        raise ConfigurationException("Have you defined all env variables needed?")