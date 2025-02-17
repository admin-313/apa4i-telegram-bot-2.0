from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: Optional[int]
    telegram_id: int
    member_since: datetime
    is_superuser: bool
    last_known_name: str | None
