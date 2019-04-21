from flask import Flask

def create_app():
    app = Flask(__name__)

    from .index import index as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')

    return app
