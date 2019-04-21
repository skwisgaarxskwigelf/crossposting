from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db.init_app(app)

    from .index import index as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')

    return app
