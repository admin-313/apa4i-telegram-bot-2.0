from dataclasses import dataclass
from datetime import datetime
from typing import Protocol, Optional

from domain.models.user import User
from domain.services.user import UserService
from application.common.interactor import Interactor
from application.user.interfaces.user_repository import UserWriter


@dataclass(frozen=True)
class AddUserDTO:
    telegram_id: int
    member_since: datetime
    is_superuser: bool
    last_known_name: Optional[str]


class UserWriteRepository(UserWriter, Protocol):
    pass


class AddUser(Interactor[AddUserDTO, None]):
    def __init__(
        self, user_writer: UserWriteRepository, user_service: UserService
    ) -> None:
        self._user_writer = user_writer
        self._user_service = user_service

    async def __call__(self, data: AddUserDTO) -> None:
        new_user: User = self._user_service.create_user(
            telegram_id=data.telegram_id,
            is_superuser=data.is_superuser,
            last_known_name=data.last_known_name,
        )
        await self._user_writer.add_user(user=new_user)