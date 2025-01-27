from pydantic import BaseModel

class BotConfiguration(BaseModel):
    bot_token: str
    admin_telegram_id: str
    link_to_fb_parser: str