from typing import Protocol
from abc import abstractmethod


class Comitter(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError
