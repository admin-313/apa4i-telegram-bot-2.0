import os
import logging
from pydantic import ValidationError
from main.exceptions import (
    BotTokenConfigurationException,
    LinkToFbParserConfigurationException,
    AdminTelegramIdConfigurationException,
)
from main.schemas import (
    BotConfiguration,
    AdminTelegramIdConfiguration,
    LinkToFbParserConfiguration,
)

logger = logging.getLogger(__name__)


def get_bot_configuration() -> BotConfiguration:
    try:
        return BotConfiguration(
            bot_token=os.getenv("BOT_TOKEN"),  # type: ignore
        )
    except ValidationError as ve:
        logger.critical(f"Could not load bot configurational variables: {str(ve)}")
        raise BotTokenConfigurationException(
            "Have you defined all env variables needed?"
        )


def get_link_to_fb_parser_configuration() -> LinkToFbParserConfiguration:
    try:
        return LinkToFbParserConfiguration(
            link_to_fb_parser=os.getenv("LINK_TO_FB_PARSER")  # type: ignore
        )
    except ValidationError as ve:
        logger.critical(
            f"Could not load facebook parser configurational variables: {str(ve)}"
        )
        raise LinkToFbParserConfigurationException(
            "Have you defined all env variables needed?"
        )


def get_admin_telegram_id_configuration() -> AdminTelegramIdConfiguration:
    try:
        return AdminTelegramIdConfiguration(
            link_to_fb_parser=os.getenv("ADMIN_TELEGRAM_ID")  # type: ignore
        )
    except ValidationError as ve:
        logger.critical(
            f"Could not load admin telegram id configurational variables: {str(ve)}"
        )
        raise AdminTelegramIdConfigurationException(
            "Have you defined all env variables needed?"
        )
