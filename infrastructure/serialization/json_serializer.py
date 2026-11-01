import json
from pathlib import Path
from datetime import datetime

from domain.models.user import User
from domain.models.chat import Chat


class JsonSerializer:

    def save(self, data: dict, file_path: str) -> None:
        path = Path(file_path)

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load(self, file_path: str) -> dict:
        path = Path(file_path)

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def save_messenger(
        self,
        users: list[User],
        chats: list[Chat],
        file_path: str
    ) -> None:
        data = {
            "users": [
                {
                    "id": user.id,
                    "username": user.username,
                    "display_name": user.display_name,
                    "status": user.status
                }
                for user in users
            ],
            "chats": [
                {
                    "id": chat.id,
                    "title": chat.title,
                    "created_at": chat.created_at.isoformat(),
                    "member_ids": chat.member_ids,
                    "is_group": chat.is_group
                }
                for chat in chats
            ]
        }

        self.save(data, file_path)

    def load_messenger(self, file_path: str) -> tuple[list[User], list[Chat]]:
        data = self.load(file_path)

        users = [
            User(
                id=item["id"],
                username=item["username"],
                display_name=item["display_name"],
                status=item["status"]
            )
            for item in data.get("users", [])
        ]

        chats = [
            Chat(
                id=item["id"],
                title=item["title"],
                created_at=datetime.fromisoformat(item["created_at"]),
                member_ids=item.get("member_ids", []),
                is_group=item.get("is_group", False)
            )
            for item in data.get("chats", [])
        ]

        return users, chats