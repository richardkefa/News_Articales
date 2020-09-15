import urllib.request, json
from .models import Articles,Sources
#getting api key
api_key = None

#geting base url
base_url = None

def Configure_request(app):
  global api_key,base_url,article_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_URL']
  article_url = app.config['ARTICLES_API_URL']
  
def get_news():
  '''
  function for getting api response
  '''
  get_news_url = base_url.format(api_key)
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
      
  return news_results

def get_articles(id):
  get_source_articles_url = article_url.format(id,api_key)
  with urllib.request.urlopen(get_source_articles_url) as url:
    articles_details_data = url.read()
    article_details_response = json.loads(articles_details_data)
    article_results = None
    if article_details_response['articles']:
      article_result_list =  article_details_response['articles']
      article_results = process_article_results(article_result_list)
    # import pdb; pdb.set_trace()

  return article_results

def process_article_results(article_list):
  article_results = []
  for article in article_list:
    id = article.get('id')
    author = article.get('author')
    title = article.get('title')
    description = article.get('description')
    fullarticle = article.get('url')
    image = article.get('urlToImage')
    publisheddate = article.get('publishedAt') 
    
    if image:
      article_object = Articles(id,author,title,image,publisheddate,fullarticle,description)
      article_results.append(article_object)
      
  return article_results 


     
    
  