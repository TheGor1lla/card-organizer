from flask import Flask

from displate.playground.playground import playground


def create_app():
    app = Flask(__name__)

    app.register_blueprint(playground)

    return app
