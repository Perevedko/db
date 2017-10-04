from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from application.models import db

from functools import wraps

import os, json


CONFIG = {
    "production": "application.config.ProductionConfig",
    "development": "application.config.DevelopmentConfig",
    "testing": "application.config.TestingConfig",
    "default": "application.config.DevelopmentConfig"
}


def configure_app(app, config_name):
    if not config_name:
        config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(CONFIG[config_name])



def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, config_name)

    return app

app = create_app()
db.init_app(app)


def json_view(func):
    """Decorator that load response data to json.

    Usage:
    @app.route("/")
    @json_view
    def index(userid=None):
        pass
    """
    @wraps(func)
    def _wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return _wrap


def auth_required(func):
    """Decorator that checks that requests
    contain an id-token in the request queery params.
    authentication failed, and have an id otherwise.

    Usage:
    @app.route("/")
    @authorized
    def secured_root():
        pass
    """
    @wraps(func)
    def _wrap(*args, **kwargs):
        token = request.args.get('token')
        if not token or token != '123qwe':
            # Unauthorized
            abort(401)
            return None
        return func(*args, **kwargs)
    return _wrap


def init_db(config_name=None):
    app = create_app(config_name)
    db = SQLAlchemy(app)
    class Datapoint(db.Model):

        __tablename__ = 'datapoints'

        __table_args__ = (
            db.UniqueConstraint("freq", "name", "date"),
        )

        id = db.Column(db.Integer, nullable=False, 
                             unique=True, 
                             autoincrement=True,
                             primary_key=True)
        freq = db.Column(db.String, nullable=False)
        name = db.Column(db.String, nullable=False)
        date = db.Column(db.String, nullable=False)


        value =db.Column(db.Float, nullable=False)
    db.create_all()
