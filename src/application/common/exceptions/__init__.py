class DatabaseException(Exception):
    pass

class UserNotFound(DatabaseException):
    pass