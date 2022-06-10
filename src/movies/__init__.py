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

    return app
