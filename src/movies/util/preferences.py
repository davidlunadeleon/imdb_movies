from movies.util.enums import MovieGenres
import numpy as np


def get_genre_value(preference_string: str) -> int:
    match preference_string:
        case "Comedy":
            return MovieGenres.COMEDY.value
        case "Drama":
            return MovieGenres.DRAMA.value
        case "Sci-Fi":
            return MovieGenres.SCI_FI.value
        case "Romantic":
            return MovieGenres.ROMANTIC.value
        case "Adventure":
            return MovieGenres.ADVENTURE.value
        case _:
            raise Exception("Unknown movie genre")


def get_preference_key(preferences) -> int:
    product = np.prod(preferences)
    return int((product % 5) + 1)
