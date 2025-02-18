from dataclasses import dataclass
from typing import Protocol


from application.common.interactor import Interactor
from application.user.interfaces.user_repository import UserWriter
from domain.models.user_id import UserId


@dataclass(frozen=True)
class DemoteUserDTO:
    user_id: UserId


class UserWriteRepository(UserWriter, Protocol):
    pass


class DemoteUser(Interactor[DemoteUserDTO, UserId]):
    def __init__(self, user_writer: UserWriteRepository) -> None:
        self._user_writer = user_writer

    async def __call__(self, data: DemoteUserDTO) -> UserId:
        await self._user_writer.demote_user(user_id=data.user_id)
        return data.user_id
