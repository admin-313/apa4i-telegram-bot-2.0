from abc import abstractmethod
from typing import Protocol

from domain.models.user import User
from domain.models.user_id import UserId


class UserReader(Protocol):
    @abstractmethod
    async def get_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError

    @abstractmethod
    async def is_in_database(self, user_id: UserId) -> bool:
        raise NotImplementedError


class UserReadWrite(UserReader, Protocol):
    @abstractmethod
    async def add_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def remove_user(self, user_id: UserId) -> None:
        raise NotImplementedError

    @abstractmethod
    async def promote_user(self, user_id: UserId) -> None:
        raise NotImplementedError

    @abstractmethod
    async def demote_user(self, user_id: UserId) -> None:
        raise NotImplementedError

    @abstractmethod
    async def add_known_name(self, name: str, user_id: UserId) -> None:
        raise NotImplementedError
