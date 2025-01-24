from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    member_since: datetime
    is_superuser: bool
    last_known_name: str