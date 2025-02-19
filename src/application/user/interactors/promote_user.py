from dataclasses import dataclass

from application.common.commiter import Commiter
from application.common.interactor import Interactor
from application.user.interfaces.user_repository import UserWriter
from domain.models.user_id import UserId


@dataclass(frozen=True)
class PromoteUserDTO:
    user_id: UserId


class PromoteUser(Interactor[PromoteUserDTO, UserId]):
    def __init__(self, user_writer: UserWriter, commiter: Commiter) -> None:
        self._user_writer = user_writer
        self._commiter = commiter

    async def __call__(self, data: PromoteUserDTO) -> UserId:
        await self._user_writer.promote_user(data.user_id)
        await self._commiter.commit()

        return data.user_id
