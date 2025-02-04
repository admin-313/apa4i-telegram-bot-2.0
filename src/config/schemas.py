from pydantic import BaseModel, HttpUrl


class BotConfiguration(BaseModel):
    bot_token: str


class AdminTelegramIdConfiguration(BaseModel):
    admin_telegram_id: int


class LinkToFbParserConfiguration(BaseModel):
    link_to_fb_parser: HttpUrl
