from typing import Protocol
from abc import abstractmethod
from domain.models.user import User
from domain.models.user_id import UserId


class UserRead(Protocol):
    @abstractmethod
    async def get_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    async def is_whitelisted(self, user_id: UserId) -> bool:
        raise NotImplementedError


class UserWrite(Protocol):
    @abstractmethod
    async def write_user(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def remove_user_by_id_if_exists(self, user_id: UserId) -> UserId:
        raise NotImplementedError

    @abstractmethod
    async def promote_if_exists(self, user_id: UserId) -> UserId:
        raise NotImplementedError

    @abstractmethod
    async def demote_if_exists(self, user_id: UserId) -> UserId:
        raise NotImplementedError
