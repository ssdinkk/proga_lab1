
from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    display_name: str
    status: str = "offline"
