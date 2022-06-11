from dataclasses import dataclass
from datetime import datetime


@dataclass(unsafe_hash=True)
class User:
    create_time: datetime
    password_hash: str
    preference_key: int
    user_id: int
    username: str
