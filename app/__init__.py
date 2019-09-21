from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    global app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = b'6hc/_gsh,./;2ZZx3c6_s,1//'
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'login_page'
    from app import views, models
    return app
