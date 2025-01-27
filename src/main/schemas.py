from pydantic import BaseModel


class BotConfiguration(BaseModel):
    bot_token: str


class AdminTelegramIdConfiguration(BaseModel):
    admin_telegram_id: str


class LinkToFbParserConfiguration(BaseModel):
    link_to_fb_parser: str
