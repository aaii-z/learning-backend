import os
from app import app
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqllite://development.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///testing.db'
 