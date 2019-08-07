from flask import Flask


app = Flask(__name__)


def create_app():
    global app
    from app import views
    return app
