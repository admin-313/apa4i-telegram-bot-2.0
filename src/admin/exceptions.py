class AdminRouterException(Exception):
    pass


class MessageInstanceNotFound(AdminRouterException):
    pass


class MessageIsEmpty(AdminRouterException):
    pass


class BotInstanceNotFound(AdminRouterException):
    pass


class UserInstanceNotFound(AdminRouterException):
    pass
