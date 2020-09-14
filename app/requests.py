import urllib.request, json
from .models import News,Sources
#getting api key
api_key = None

#geting base url
base_url = None

def Configure_request(app):
  global api_key,base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_URL']
  
def get_news(category):
  '''
  function for getting api response
  '''
  get_news_url = base_url.format(category,api_key)
  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)
    
    news_results = None
    
    if get_news_response['sources']:
      news_results_list = get_news_response['sources']
      news_results = process_results(news_results_list)
  
  return news_results

def process_results(news_list):
  '''
  function that processes the news result and transform them to a list of Objects
  Args:
      news_list: a list of dictionaries that contain news details
  Returns:
      news_results: a list of news objects    
  '''
  news_results = []
  for news_item in news_list:
    id = news_item.get('id')
    name = news_item.get('name')
    description = news_item.get('description')
    url = news_item.get('url')
    category = news_item.get('category')
    language = news_item.get('language')

    
    if id:
      news_object = Sources(id,name,description,url,category,language)
      news_results.append(news_object)
    print(news_item)

  return news_results
    
  