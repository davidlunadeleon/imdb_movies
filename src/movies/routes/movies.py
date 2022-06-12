from flask import Blueprint, g, jsonify, request as req
from movies.repository import MovieRepository, UserRepository
from movies.util.math import clamp
from movies.middlewares.auth import require_login

bp = Blueprint("movies", __name__, url_prefix="/movies")

user_repository: UserRepository
user_repository = g.user_repository

movie_repository: MovieRepository
movie_repository = g.movie_repository


@bp.route("/recommendations", methods=["GET"])
@require_login
def recommendations():
    """
    Returns movie recommendations matching the user's preference key

    :param num: amount of movies to return. If none is provided it will return 10 movie recommendations.
    """ 
    num_rec = req.args.get("num")
    num_rec = 10 if num_rec is None else clamp(int(num_rec), 1, 1000)

    user = g.user
    selected_movies = list(
        filter(
            lambda movie: movie.preference_key == user.preference_key,
            movie_repository.list(),
        )
    )[:num_rec]
    return jsonify(selected_movies)
