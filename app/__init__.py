from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.entrypoints.config.Config')
    db.init_app(app)

    from app.entrypoints.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app