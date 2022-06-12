from flask import Blueprint, g, jsonify, request as req
from movies.repository import MovieRepository, UserRepository
from movies.util.math import clamp
from movies.middlewares.auth import require_login

bp = Blueprint("media", __name__, url_prefix="/media")

user_repository: UserRepository
user_repository = g.user_repository

movie_repository: MovieRepository
movie_repository = g.movie_repository


@bp.route("/recommendations", methods=["GET"])
@require_login
def recommendations():
    """
    Returns media recommendations matching the user's preference key

    :param num: amount of media to return. If none is provided it will return 10 media recommendations.
    """
    match req.args.get("media_type"):
        case None:
            repository = movie_repository
        case "movies":
            repository = movie_repository
        case _:
            raise Exception("Unkown media type")

    num_rec = req.args.get("num")
    num_rec = 10 if num_rec is None else clamp(int(num_rec), 1, 1000)
    match req.args.get("order"):
        case None:
            is_descending = False
        case "asc":
            is_descending = False
        case "desc":
            is_descending = True
        case _:
            raise Exception("Unkown order")

    user = g.user
    selected_media = list(
        filter(
            lambda media: media.preference_key == user.preference_key,
            repository.list(),
        )
    )
    selected_media = sorted(selected_media, key=lambda media: media.rating)
    if is_descending:
        selected_media.reverse()
    selected_media = selected_media[:num_rec]

    return jsonify(selected_media)
