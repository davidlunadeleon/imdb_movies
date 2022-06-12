from flask import Flask, g
from movies.repository import UserRepository, MovieRepository
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from movies.services import db

    session = db.start_mappers()

    # TODO: Move to env file
    app.secret_key = "0a5a98bac7adcad722b3f29b3ff37a288277de1cf34d803106f3860fc548287c"

    with app.app_context():
        g.movie_repository = MovieRepository(session)
        g.user_repository = UserRepository(session)

        g.movie_repository.populate()

        from movies.routes import auth, movies

        app.register_blueprint(auth.bp)
        app.register_blueprint(movies.bp)

    return app
