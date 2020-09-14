import os

class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_URL ='http://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
  NEWS_API_KEY = os.environ.get('API_KEY')
  
class ProdConfig(Config):
  '''
  production configuration child class 
  
  Args:
    config: The parent configuration Class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  Args:
      Config: The parent configuration class with General configuration settings
  '''
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig
}