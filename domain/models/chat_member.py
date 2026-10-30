
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ChatMember:
    id: int
    chat_id: int
    user_id: int
    joined_at: datetime
    role: str = "member"
