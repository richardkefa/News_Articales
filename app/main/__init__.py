from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors


def creat_app(config_name):
  #initializing application
  app = Flask(__name__)

  #setting up configuration
  app.config.from_object(config_options[config_name])

  # Registering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  return app