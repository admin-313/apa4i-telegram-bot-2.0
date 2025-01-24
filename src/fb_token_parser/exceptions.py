class FBParserException(Exception):
    pass


class FBParserTimeout(FBParserException):
    pass


class FBConnectionFailed(FBParserException):
    pass
