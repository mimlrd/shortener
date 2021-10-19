import os
from flask import Flask
from flask_restful import Api
from rest.config import config

api = Api()
## general config
app_config = config[os.environ.get('FLASK_ENV', 'default')]

from pymongo import MongoClient, errors
mongo_client = MongoClient(app_config.MONGO_URI, connect=False)

def create_app(config_name):

    print(f'Starting app in {config_name} environment')
    app = Flask(__name__)
    #api = Api(app)
    app.config.from_object(config.get(config_name))

    from rest.shorten.views import shorten_blueprint
    app.register_blueprint(shorten_blueprint)
    

    return app 

