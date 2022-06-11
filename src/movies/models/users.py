from datetime import datetime


class User:
    create_time: datetime
    password_hash: str
    preference_key: int
    user_id: int
    username: str

    def __init__(
        self,
        create_time: datetime,
        password_hash: str,
        preference_key: int,
        user_id: int,
        username: str,
    ) -> None:
        self.create_time = create_time
        self.password_hash = password_hash
        self.preference_key = preference_key
        self.user_id = user_id
        self.username = username
