from flask import Blueprint, request, g
from flask.wrappers import Response
from movies.middlewares.auth import require_login
from movies.models.users import User
from movies.repository import UserRepository
from movies.util.preferences import get_preference_key, get_genre_value

bp = Blueprint("users", __name__, url_prefix="/users")

user_repository: UserRepository
user_repository = g.user_repository


@bp.route("/<int:user_id>", methods=["PUT"])
@require_login
def update_user(user_id: int):
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
    username = request.form["username"]

    user = g.user
    if user_id == user.user_id:
        user_repository.update(
            User(username, preference_key, password, user_id=user_id)
        )
        return Response(status=200)
    else:
        return Response(status=403)
