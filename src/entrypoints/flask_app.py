from flask import Flask

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    return "Hello World!", 200
