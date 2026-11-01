from datetime import datetime

from domain.models.user import User
from domain.models.chat import Chat

from infrastructure.serialization.json_serializer import JsonSerializer
from infrastructure.serialization.xml_serializer import XmlSerializer


def create_test_data():
    users = [
        User(
            id=1,
            username="alex",
            display_name="Алекс",
            status="online"
        ),
        User(
            id=2,
            username="maria",
            display_name="Мария",
            status="offline"
        )
    ]

    chats = [
        Chat(
            id=1,
            title="Общий чат",
            created_at=datetime(2026, 11, 1, 12, 0, 0),
            member_ids=[1, 2],
            is_group=True
        )
    ]

    return users, chats


def test_json_save_and_load(tmp_path):
    users, chats = create_test_data()
    file_path = tmp_path / "messenger.json"

    serializer = JsonSerializer()

    serializer.save_messenger(users, chats, str(file_path))
    loaded_users, loaded_chats = serializer.load_messenger(str(file_path))

    assert loaded_users == users
    assert loaded_chats == chats


def test_xml_save_and_load(tmp_path):
    users, chats = create_test_data()
    file_path = tmp_path / "messenger.xml"

    serializer = XmlSerializer()

    serializer.save_messenger(users, chats, str(file_path))
    loaded_users, loaded_chats = serializer.load_messenger(str(file_path))

    assert loaded_users == users
    assert loaded_chats == chats


def test_json_empty_data(tmp_path):
    file_path = tmp_path / "empty.json"

    serializer = JsonSerializer()

    serializer.save_messenger([], [], str(file_path))
    users, chats = serializer.load_messenger(str(file_path))

    assert users == []
    assert chats == []


def test_xml_empty_data(tmp_path):
    file_path = tmp_path / "empty.xml"

    serializer = XmlSerializer()

    serializer.save_messenger([], [], str(file_path))
    users, chats = serializer.load_messenger(str(file_path))

    assert users == []
    assert chats == []