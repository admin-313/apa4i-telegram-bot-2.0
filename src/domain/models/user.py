from dataclasses import dataclass
from datetime import datetime
from domain.models.user_id import UserId

@dataclass
class User:
    id: UserId
    member_since: datetime
    is_superuser: bool
    last_known_name: str | None