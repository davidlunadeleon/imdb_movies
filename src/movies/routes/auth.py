from datetime import datetime
from flask import Blueprint, request, current_app as app
from flask.wrappers import Response
from movies.models.users import User
from movies.repository import UserRepository
from movies.util.enums import MovieGenres
from random import randint
import numpy as np

bp = Blueprint("auth", __name__, url_prefix="/auth")


def get_preference_key(preferences) -> int:
    product = np.prod(preferences)
    return int((product % 5) + 1)


def get_genre(preference_string: str) -> int:
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


@bp.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    preference1 = request.form["preference1"]
    preference2 = request.form["preference2"]
    preference3 = request.form["preference3"]
    create_time = datetime.now()
    preference_key = get_preference_key(
        [get_genre(preference1), get_genre(preference2), get_genre(preference3)]
    )

    user = User(password, preference_key, username)
    repo = UserRepository(app.session)
    repo.add(user)
    app.session.commit()
    l = repo.list()
    print(l)
    return Response(response="ok", status=200)
