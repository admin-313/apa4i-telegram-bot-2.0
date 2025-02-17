from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from domain.models.user import User
from domain. import 
from application.common.interactor import Interactor
from application.user.interfaces.user_repository import UserWriter


@dataclass(frozen=True)
class AddUserDTO:
    telegram_id: int
    member_since: datetime
    is_superuser: bool
    last_known_name: str | None = None


class UserWriteRepository(UserWriter, Protocol):
    pass


class AddUser(Interactor[AddUserDTO, None]):
    def __init__(self, user_writer: UserWriteRepository, user_service: ) -> None:
        self._user_read_write = user_writer
        self._user_service = 
    async def __call__(self, data: AddUserDTO) -> None:
        new_user = User(
            id=None,
            telegram_id=data.telegram_id,
            member_since=data.member_since,
            is_superuser=data.is_superuser,
            last_known_name=data.last_known_name,
        )
