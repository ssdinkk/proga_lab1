
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Chat:
    id: int
    title: str
    created_at: datetime
    member_ids: list[int] = field(default_factory=list)
    is_group: bool = False
