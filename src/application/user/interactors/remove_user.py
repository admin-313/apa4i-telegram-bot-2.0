from dataclasses import dataclass

from application.common.commiter import Commiter
from application.common.interactor import Interactor
from application.user.interfaces.user_repository import UserWriter
from domain.models.user_id import UserId


@dataclass(frozen=True)
class RemoveUserDTO:
    user_id: UserId


class RemoveUser(Interactor[RemoveUserDTO, UserId]):
    def __init__(self, user_writer: UserWriter, commiter: Commiter) -> None:
        self._user_writer = user_writer
        self._commiter = commiter

    async def __call__(self, data: RemoveUserDTO) -> UserId:
        await self._user_writer.remove_user(data.user_id)
        await self._commiter.commit()

        return data.user_id
