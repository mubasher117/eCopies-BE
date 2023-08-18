from enum import Enum


class ErrorMessage(Enum):
    def __new__(cls, code, message):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.code = code
        obj.message = message
        return obj

    UNKNOWN_ERROR = (10001, 'An error occurred, please try again')
    INVALID_AUTH = (10002, 'Invalid authentication')
    NOT_AUTH = (10003, 'Authentication required to access this feature')
    NOT_PERMISSION = (10004, 'You do not have permission to perform this action')
    THROTTLED_REQUEST = (10005, 'Access restricted, you may have made too many requests at this time')
    NOT_FOUND = (10006, 'Record not found')
    NOT_ALLOW_METHOD = (10007, 'This method is not allowed')
    LOGIN_FAIL = (10008, 'Incorrect username or password')
