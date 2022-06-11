from flask import Blueprint, request

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    preference1 = request.form["request1"]
    preference2 = request.form["request2"]
    preference3 = request.form["request3"]
