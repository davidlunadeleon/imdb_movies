from functools import wraps
from flask import session, g
from flask.wrappers import Response
from movies.repository import UserRepository

user_repository: UserRepository
user_repository = g.user_repository


def require_login(func):
    @wraps(func)
    def check_user_id(*args, **kwargs):
        user_id = session.get("user_id")
        if user_id is not None:
            user_id = int(user_id)
            g.user = user_repository.get_by_id(user_id)
            return func(*args, **kwargs)
        else:
            return Response(status=401)

    return check_user_id
