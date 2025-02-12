from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from domain.common.interfaces.database import Database
from infrastructure.config import DatabaseConfig


class SQLAlchemyDatabase(Database[AsyncSession]):
    def __init__(self, config: DatabaseConfig) -> None:
        self._engine: AsyncEngine = create_async_engine(url=config.url)
        self._session_factory = async_sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_factory() as session, session.begin():
            yield session
