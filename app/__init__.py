from flask import Flask
from config import config_options

def creat_app(config_name):
  #initializing application
  app = Flask(__name__)

  #setting up configuration
  app.config.from_object(config_options[config_name])

  return app