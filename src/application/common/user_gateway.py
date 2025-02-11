from typing import Protocol
from domain.models.user import User
from domain.models.user_id import UserId


class UserRead(Protocol):
    async def get_by_id(self, user_id: UserId) -> User:
        ...

    async def get_all_users(self) -> list[User]:
        ...

    async def is_whitelisted(self, user_id: UserId) -> bool:
        ...


class UserWrite(Protocol):
    async def write_user(self, user: User) -> User:
        ...

    async def remove_user_by_id_if_exists(self, user_id: UserId) -> UserId:
        ...

    async def promote_if_exists(self, user_id: UserId) -> UserId:
        ...

    async def demote_if_exists(self, user_id: UserId) -> UserId:
        ...
