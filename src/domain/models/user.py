from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    telegram_id: int
    member_since: datetime
    is_superuser: bool
    last_known_name: str | None
