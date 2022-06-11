from dataclasses import dataclass
from datetime import datetime


@dataclass(unsafe_hash=True)
class Movie:
    create_time: datetime
    movie_id: int
    movie_title: str
    preference_key: int
    rating: float
    year: int
