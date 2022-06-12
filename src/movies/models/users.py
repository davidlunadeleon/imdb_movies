from dataclasses import dataclass, InitVar
from datetime import datetime
from movies.util.password import hash


@dataclass(unsafe_hash=True)
class User:
    username: str
    preference_key: int
    password: InitVar[str]
    user_id: int | None = None
    create_time: datetime | None = None
    password_hash: bytes | None = None

    def __post_init__(self, password: str):
        self.create_time = datetime.now()
        self.password_hash = hash(password)
