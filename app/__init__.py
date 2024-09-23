from flask import Flask
app = Flask(__name__)
from app import views
from app import config
app.config.from_object(config.DevelopmentConfig)
#app.config.from_object('config.DevelopmentConfig')