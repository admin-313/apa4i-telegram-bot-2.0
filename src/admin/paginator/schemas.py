from typing import Any
from pydantic import BaseModel

class PaginatorResponce(BaseModel):
    page_elements: list[Any]
    is_next_page: bool
    current_page: int