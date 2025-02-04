class AdminRouterException(Exception):
    pass

class BlankMessageException(AdminRouterException):
    pass

class BotInstanceNotFound(AdminRouterException):
    pass