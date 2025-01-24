from pydantic import BaseModel, PositiveInt
from datetime import datetime


class User(BaseModel):
    id: PositiveInt
    member_since: datetime
    is_superuser: bool
    last_known_name: str
