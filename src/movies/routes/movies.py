from flask import Blueprint, g, jsonify
from movies.repository import MovieRepository, UserRepository

bp = Blueprint("movies", __name__, url_prefix="/movies")

user_repository: UserRepository
user_repository = g.user_repository

movie_repository: MovieRepository
movie_repository = g.movie_repository


@bp.route("/recommendations/<id>", methods=["GET"])
def recommendations(id: int):
    user = user_repository.get_by_id(id)
    selected_movies = list(
        filter(
            lambda movie: movie.preference_key == user.preference_key,
            movie_repository.list(),
        )
    )
    return jsonify(selected_movies)
