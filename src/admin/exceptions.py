class AdminRouterException(Exception):
    pass

class MessageInstanceNotFound(AdminRouterException):
    pass

class BotInstanceNotFound(AdminRouterException):
    pass