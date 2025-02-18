from dataclasses import dataclass
from typing import Protocol

from application.common.interactor import Interactor
from application.user.interfaces.user_repository import UserReader
from domain.models.user_id import UserId


@dataclass(frozen=True)
class IsWhitelistedDTO:
    user_id: UserId


class UserReadRepository(UserReader, Protocol):
    pass


class IsWhitelisted(Interactor[IsWhitelistedDTO, bool]):
    def __init__(self, user_reader: UserReadRepository) -> None:
        self._user_reader = user_reader

    async def __call__(self, data: IsWhitelistedDTO) -> bool:
        return await self._user_reader.is_in_database(data.user_id)
