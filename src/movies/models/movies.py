from datetime import datetime


class Movie:
    create_time: datetime
    movie_id: int
    movie_title: str
    preference_key: int
    rating: float
    year: int

    def __init__(
        self,
        create_time: datetime,
        movie_id: int,
        movie_title: str,
        preference_key: int,
        rating: float,
        year: int,
    ) -> None:
        self.create_time = create_time
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.preference_key = preference_key
        self.rating = rating
        self.year = year
