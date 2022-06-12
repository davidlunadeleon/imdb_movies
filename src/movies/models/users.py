from dataclasses import dataclass
from datetime import datetime


@dataclass(unsafe_hash=True)
class User:
    password_hash: str
    preference_key: int
    username: str
    create_time: datetime | None = None
    user_id: int | None = None

    def __post_init__(self):
        self.create_time = datetime.now()
