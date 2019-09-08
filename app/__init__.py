from flask import Flask


app = Flask(__name__)
app.secret_key = b'6hc/_gsh,./;2ZZx3c6_s,1//'


def create_app():
    global app
    from app import views
    return app
