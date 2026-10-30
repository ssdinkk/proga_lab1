
from dataclasses import dataclass


@dataclass
class Contact:
    id: int
    owner_id: int
    contact_user_id: int
    nickname: str = ""
