from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from infrastructure.persistence.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    member_since: Mapped[datetime]
    is_superuser: Mapped[bool] = mapped_column(nullable=False)
    last_known_name: Mapped[str] = mapped_column(String(23), nullable=True)
