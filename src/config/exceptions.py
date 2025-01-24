class ConfigException(Exception):
    pass

class WhitelistConfigException(ConfigException):
    pass

class WhitelistConfigFileNotFound(ConfigException):
    pass