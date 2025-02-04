class PaginatorException(Exception):
    pass


class PageNotFound(PaginatorException):
    pass


class PageCantBeZero(PaginatorException):
    pass
