class MessengerException(Exception):
    pass


class UserNotFoundException(MessengerException):
    pass


class ChatNotFoundException(MessengerException):
    pass

class DuplicateEntityException(MessengerException):
    pass