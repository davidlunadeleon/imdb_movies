from flask import Blueprint, request, g
from flask.wrappers import Response
from movies.models.users import User
from movies.repository import UserRepository
from movies.util.preferences import get_preference_key, get_genre_value

bp = Blueprint("auth", __name__, url_prefix="/auth")

user_repository: UserRepository
user_repository = g.user_repository


@bp.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    preference1 = request.form["preference1"]
    preference2 = request.form["preference2"]
    preference3 = request.form["preference3"]
    preference_key = get_preference_key(
        [
            get_genre_value(preference1),
            get_genre_value(preference2),
            get_genre_value(preference3),
        ]
    )

    user_repository.add(User(username, preference_key, password))
    return Response(response="ok", status=200)
