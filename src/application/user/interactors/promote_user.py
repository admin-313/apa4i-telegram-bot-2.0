from dataclasses import dataclass
from typing import Protocol

from application.common.interactor import Interactor
from application.user.interfaces.user_repository import UserWriter
from domain.models.user_id import UserId


@dataclass(frozen=True)
class PromoteUserDTO:
    user_id: UserId


class UserWriteRepository(UserWriter, Protocol):
    pass


class PromoteUser(Interactor[PromoteUserDTO, UserId]):
    def __init__(self, user_writer: UserWriteRepository) -> None:
        self._user_writer = user_writer

    async def __call__(self, data: PromoteUserDTO) -> UserId:
        await self._user_writer.promote_user(data.user_id)
        return data.user_id
