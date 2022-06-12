from dataclasses import dataclass
from datetime import datetime


@dataclass(unsafe_hash=True)
class Movie:
    """ This class is used to hold Movie objects information."""
    movie_title: str
    preference_key: int
    rating: float
    year: int
    create_time: datetime | None = None
    movie_id: int | None = None

    def __post_init__(self):
        self.create_time = datetime.now()
