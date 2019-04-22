from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
#    app.config.from_object(os.environ['APP_SETTINGS'])
#    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    from crossposting import models    

    from .index import index as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')

    return app
