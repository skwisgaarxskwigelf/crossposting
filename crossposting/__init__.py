from flask import Flask
app = Flask(__name__)

import crossposting.views

#def create_app(config_name):
#    app = Flask(__name__)
#    app.config.from_object(app_config[config_name])
#    return app
