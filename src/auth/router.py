from aiogram import Router
from auth.auth_middleware import AuthMiddleware
from auth.database.json_driver.drivers import JSONConfigReader
from auth.database.dispatcher import database_service_dispatcher


middleware_router = Router()

config_reader: JSONConfigReader = database_service_dispatcher["json_readonly"]()

middleware_router.message.outer_middleware(AuthMiddleware(config_reader))
