from movies.util.enums import MovieGenres
import numpy as np


def get_genre_value(preference_string: str) -> int:
    """
    Get the movie genre value

    :param preference_string: string of the movie genre
    :returns the movie's genre value
    """ 
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
    """
    Calculates the user's preference key

    :param preferences: array containing the keys of the user's movie preferences
    :returns the preference key
    """ 
    product = np.prod(preferences)
    return int((product % 5) + 1)
