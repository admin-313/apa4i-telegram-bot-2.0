from typing import Any
from pydantic import BaseModel

class PaginatorResponse(BaseModel):
    page_elements: list[Any]
    current_page: int
    total_pages: int