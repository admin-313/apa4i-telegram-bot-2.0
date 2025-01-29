import logging
from aiogram import Dispatcher
from root.router import root_router
from invisible_text.router import invisible_text_router
from auth.router import middleware_router

logger = logging.getLogger(__name__)


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_routers(middleware_router, root_router, invisible_text_router)
    return dp
