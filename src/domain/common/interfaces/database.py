from abc import ABC, abstractmethod
from typing import Generic, TypeVar, AsyncContextManager


SessionType = TypeVar("SessionType")


class Database(ABC, Generic[SessionType]):
    """So we are using Generic here basically because
    we may want to have multiple session types based on what db we choose.
    In our scope it allows for using both the async ans sync alchemy's session types.
    To pass them we use Database[AsyncSession] or Database[SyncSession]
    in the infrastructure layer"""

    @abstractmethod
    def get_session(self) -> AsyncContextManager[SessionType]:
        raise NotImplementedError

    @abstractmethod
    async def dispose(self) -> None:
        raise NotImplementedError
