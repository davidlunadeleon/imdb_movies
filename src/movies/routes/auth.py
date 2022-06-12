from flask import Blueprint, request, g, session
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


@bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = user_repository.get_by_username(username)
    if user.check_credentials(username, password):
        session["user_id"] = user.user_id
        return Response(status=200)
    else:
        return Response(response="Wrong user credentials provided", status=401)
