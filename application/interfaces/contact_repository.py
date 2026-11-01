from abc import ABC, abstractmethod

from domain.models.contact import Contact


class ContactRepository(ABC):

    @abstractmethod
    def add(self, contact: Contact) -> None:
        pass

    @abstractmethod
    def get_by_id(self, contact_id: int) -> Contact | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Contact]:
        pass

    @abstractmethod
    def update(self, contact: Contact) -> None:
        pass

    @abstractmethod
    def delete(self, contact_id: int) -> None:
        pass

    @abstractmethod
    def get_by_owner(self, owner_id: int) -> list[Contact]:
        pass