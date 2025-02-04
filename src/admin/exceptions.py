class AdminRouterException(Exception):
    pass

class MessageInstanceNotFound(AdminRouterException):
    pass

class MessageisEmpty(AdminRouterException):
    pass

class BotInstanceNotFound(AdminRouterException):
    pass

class UserInstanceNotFound(AdminRouterException):
    pass