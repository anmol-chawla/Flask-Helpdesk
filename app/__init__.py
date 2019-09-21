from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    global app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate.init_app(app, db)
    from app import views, models
    return app
