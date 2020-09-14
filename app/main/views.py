from flask import render_template,request,redirect,url_for
from . import main
from ..models import News
from ..requests import get_news 

@main.route('/')
def index():
  '''
  View root page function that returns the index page
  '''
  business_news = get_news('business')
  politics_news = get_news('politics')
  sports_news = get_news('sports')
  
  return render_template('index.html',business = business_news,politics = politics_news,sports = sports_news)