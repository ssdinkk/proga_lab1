
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Notification:
    id: int
    user_id: int
    message: str
    created_at: datetime
    is_read: bool = False
