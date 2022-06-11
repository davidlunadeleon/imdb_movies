from flask import Flask
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from movies.services import db

    db.start_mappers()

    from movies.routes import auth, movies

    app.register_blueprint(auth.bp)
    app.register_blueprint(movies.bp)

    return app
