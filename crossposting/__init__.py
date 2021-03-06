from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from config import app_config
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    Bootstrap(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    from crossposting import models    

    from .index import index as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')

    from .posts import posts_page as posts_blueprint
    app.register_blueprint(posts_blueprint, url_prefix='/posts')

    return app
