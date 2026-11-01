import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

from domain.models.user import User
from domain.models.chat import Chat


class XmlSerializer:

    def save_messenger(
        self,
        users: list[User],
        chats: list[Chat],
        file_path: str
    ) -> None:
        root = ET.Element("messenger")

        users_element = ET.SubElement(root, "users")

        for user in users:
            user_element = ET.SubElement(users_element, "user")

            ET.SubElement(user_element, "id").text = str(user.id)
            ET.SubElement(user_element, "username").text = user.username
            ET.SubElement(user_element, "display_name").text = user.display_name
            ET.SubElement(user_element, "status").text = user.status

        chats_element = ET.SubElement(root, "chats")

        for chat in chats:
            chat_element = ET.SubElement(chats_element, "chat")

            ET.SubElement(chat_element, "id").text = str(chat.id)
            ET.SubElement(chat_element, "title").text = chat.title
            ET.SubElement(
                chat_element,
                "created_at"
            ).text = chat.created_at.isoformat()

            ET.SubElement(
                chat_element,
                "is_group"
            ).text = str(chat.is_group).lower()

            members_element = ET.SubElement(chat_element, "member_ids")

            for member_id in chat.member_ids:
                ET.SubElement(
                    members_element,
                    "member_id"
                ).text = str(member_id)

        tree = ET.ElementTree(root)

        ET.indent(tree, space="    ")

        path = Path(file_path)
        tree.write(path, encoding="utf-8", xml_declaration=True)

    def load_messenger(
        self,
        file_path: str
    ) -> tuple[list[User], list[Chat]]:

        path = Path(file_path)
        tree = ET.parse(path)
        root = tree.getroot()

        users = []

        users_element = root.find("users")

        if users_element is not None:
            for user_element in users_element.findall("user"):
                user = User(
                    id=int(user_element.findtext("id")),
                    username=user_element.findtext("username"),
                    display_name=user_element.findtext("display_name"),
                    status=user_element.findtext("status", "offline")
                )

                users.append(user)

        chats = []

        chats_element = root.find("chats")

        if chats_element is not None:
            for chat_element in chats_element.findall("chat"):
                members_element = chat_element.find("member_ids")

                member_ids = []

                if members_element is not None:
                    member_ids = [
                        int(member.text)
                        for member in members_element.findall("member_id")
                    ]

                chat = Chat(
                    id=int(chat_element.findtext("id")),
                    title=chat_element.findtext("title"),
                    created_at=datetime.fromisoformat(
                        chat_element.findtext("created_at")
                    ),
                    member_ids=member_ids,
                    is_group=(
                        chat_element.findtext("is_group", "false") == "true"
                    )
                )

                chats.append(chat)

        return users, chats