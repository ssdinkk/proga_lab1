
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    id: int
    chat_id: int
    sender_id: int
    text: str
    created_at: datetime
    is_read: bool = False
