# -*- coding: utf-8 -*-
## config.py

'''
  "Configuration for the app"
  SQLALCHEMY_DATABASE_URI could be different for Development or Production
  2 Different Classes :
  - Development
  - Production
'''

import os
import secrets
from dotenv import load_dotenv

from pathlib import Path  
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
   API_PREFIX = '/api'
   TESTING = False
   DEBUG = False

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No secret key set for Flask application")
        
    ## MONGODB
    MONGOHOST = os.environ.get('MONGOHOST')
    MONGOPORT = os.environ.get('MONGOPORT')
    MONGOUSER = os.environ.get('MONGOUSER')
    MONGOPASSWORD = os.environ.get('MONGOPASSWORD')

    MONGO_URI = 'mongodb://' + MONGOUSER + ':' + MONGOPASSWORD + '@' + MONGOHOST + ':' + str(MONGOPORT) + '/'

    if not MONGO_URI:
        raise ValueError('Missing the MongoDB host uri')

    ## Response format - Deafult: JSON
    RESPONSE_FORMAT = os.environ.get('RESPONSE_FORMAT', 'json')

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
    


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False

class TestingConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}