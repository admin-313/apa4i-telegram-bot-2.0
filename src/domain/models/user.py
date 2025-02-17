from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.models.user_id import UserId


@dataclass
class User:
    id: Optional[UserId]
    telegram_id: int
    member_since: datetime
    is_superuser: bool
    last_known_name: Optional[str]
