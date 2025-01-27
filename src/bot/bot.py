from aiogram import Dispatcher
from bot.router import root_router
from invisible_text.router import invisible_text_router

def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_routers(root_router, invisible_text_router)
    return dp
