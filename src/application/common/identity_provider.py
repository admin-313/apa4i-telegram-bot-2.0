from abc import abstractmethod
from typing import Protocol
from domain.models.user import User


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_user(self) -> User:
        raise NotImplementedError
    