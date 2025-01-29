from aiogram import Router
from auth.auth_middleware import AuthMiddleware
from src.auth.database.json_driver.drivers import JSONConfigReader

# TODO Переместить ридеры конфигов в auth модуль
middleware_router = Router()

middleware_router.message.outer_middleware(AuthMiddleware(JSONConfigReader()))
