from typing import AsyncContextManager
from abc import ABC, abstractmethod

from application.user.interactors.add_user import AddUser
from application.user.interactors.demote_user import DemoteUser
from application.user.interactors.is_admin import IsAdmin
from application.user.interactors.is_whitelisted import IsWhitelisted
from application.user.interactors.remove_user import RemoveUser
from application.user.interactors.promote_user import PromoteUser


class InteractorFactory(ABC):
    @abstractmethod
    async def add_user(self) -> AsyncContextManager[AddUser]:
        raise NotImplementedError

    @abstractmethod
    async def demote_user(self) -> AsyncContextManager[DemoteUser]:
        raise NotImplementedError

    @abstractmethod
    async def is_admin(self) -> AsyncContextManager[IsAdmin]:
        raise NotImplementedError

    @abstractmethod
    async def is_whitelisted(self) -> AsyncContextManager[IsWhitelisted]:
        raise NotImplementedError

    @abstractmethod
    async def remove_user(self) -> AsyncContextManager[RemoveUser]:
        raise NotImplementedError

    @abstractmethod
    async def promote_user(self) -> AsyncContextManager[PromoteUser]:
        raise NotImplementedError
