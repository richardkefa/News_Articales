from flask import Flask
from config import config_options

def creat_app(config_name):
  #initializing application
  app = Flask(__name__)

  #setting up configuration
  app.config.from_object(config_options[config_name])
  
  #registering the blue print
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  #setting  config
  from .requests import Configure_request
  Configure_request(app)

  return app