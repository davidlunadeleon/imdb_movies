from dataclasses import dataclass, InitVar
from datetime import datetime
from movies.util.password import hash, compare


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

    def check_credentials(self, username: str, password: str) -> bool:
        return (
            self.username == username
            and self.password_hash is not None
            and compare(self.password_hash, password)
        )
