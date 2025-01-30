import logging
from aiogram import Dispatcher
from root.router import root_router
from invisible_text.router import invisible_text_router
from auth.router import auth_middleware_router
from admin.router import admin_commands_router

logger = logging.getLogger(__name__)


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_routers(
        auth_middleware_router,
        admin_commands_router,
        root_router,
        invisible_text_router,
    )
    return dp
