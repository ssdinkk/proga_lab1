
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Reaction:
    id: int
    message_id: int
    user_id: int
    emoji: str
    created_at: datetime
