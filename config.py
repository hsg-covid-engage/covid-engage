import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'abcdefgh'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class TestingConfig(Config):
    TESTING = True

