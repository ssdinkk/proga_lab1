
from dataclasses import dataclass


@dataclass
class Attachment:
    id: int
    message_id: int
    file_name: str
    file_path: str
    file_type: str
