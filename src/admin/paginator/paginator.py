import math
from typing import Any
from admin.paginator.exceptions import PageCantBeZero
from admin.paginator.schemas import PaginatorResponce
from auth.database.json_driver.drivers import JSONConfigReader


class Paginator:
    def __init__(self, elements_per_page: int, db_reader: JSONConfigReader) -> None:
        self.elements_per_page: int = elements_per_page
        self.db_reader: JSONConfigReader = db_reader

    def get_page(self, target_page: int) -> PaginatorResponce:
        max_pages: int = self.get_maximum_amount_of_pages()
        all_elements: list[Any] = self.db_reader.get_whitelisted_users()

        if not target_page:
            raise PageCantBeZero("Page can't be zero")
        if target_page > max_pages:
            target_page = max_pages

        start_index: int = (target_page - 1) * self.elements_per_page
        end_index: int = target_page * self.elements_per_page

        return PaginatorResponce(
            page_elements=all_elements[start_index:end_index],
            is_next_page=target_page < max_pages,
            current_page=target_page,
        )

    def get_maximum_amount_of_pages(self) -> int:
        elements: list[Any] = self.db_reader.get_whitelisted_users()
        return (
            math.ceil(
                len(self.db_reader.get_whitelisted_users()) / self.elements_per_page
            )
            if elements
            else 0
        )
