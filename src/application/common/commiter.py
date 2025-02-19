from typing import Protocol
from abc import abstractmethod


class Commiter(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError
