class MessengerException(Exception):
    """Базовое исключение мессенджера."""


class UserNotFoundException(MessengerException):
    """Пользователь не найден."""


class ChatNotFoundException(MessengerException):
    """Чат не найден."""


class MessageNotFoundException(MessengerException):
    """Сообщение не найдено."""


class DuplicateEntityException(MessengerException):
    """Попытка создать дублирующую сущность."""


class ContactNotFoundException(MessengerException):
    """Контакт не найден."""


class AttachmentNotFoundException(MessengerException):
    """Вложение не найдено."""


class InvalidMessageException(MessengerException):
    """Некорректное сообщение."""


class SerializationException(MessengerException):
    """Ошибка сериализации или десериализации данных."""

class ChatMemberNotFoundException(MessengerException):
    """Участник чата не найден."""

class ReactionNotFoundException(MessengerException):
    """Реакция не найдена."""

class NotificationNotFoundException(MessengerException):
    """Уведомление не найдено."""