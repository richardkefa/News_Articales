from flask import render_template,request,redirect,url_for
from . import main
from ..models import Articles,Sources
from ..requests import get_news,get_articles

@main.route('/')
def index():
  '''
  View root page function that returns the index page
  '''
  source_news = get_news()
  # business_news = get_news('business')
  # politics_news = get_news('entertainment')
  # sports_news = get_news('sports')
  # print(business_news)
  
  return render_template('index.html',source = source_news)
@main.route('/article/<string:id>')
def aricles(id):
  '''
  view article page for a source
  '''
  articles = get_articles(id)
  # title = f'{articles.title}'
  
  return render_template('articles.html',articles = articles)