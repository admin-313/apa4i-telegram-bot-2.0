import pathlib

from pydantic import TypeAdapter
from config.schemas import User

class JSONConfigReader():

    def __init__(self) -> None:
        pass

    def get_whitelisted_users() -> list[User]:
        pass
            
    def _get_users_config() -> str:
        json_string: str = 

class JSONConfigWriter():
