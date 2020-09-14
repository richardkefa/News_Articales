class Articles:
  '''
  News class to define news object
  '''
  def __init__(self,id,author,title,image,publishedate,fullarticle,description):
    
    self.id = id
    self.author = author
    self.title = title
    self.description = description
    self.image = 'https://s3.cointelegraph.com/storage/uploads/view/8e448214efbe933b0206231406073645.jpg'
    self.publishedate = '2017-09-28 16:06:30.439388'
    self.fullarticle = 'https://cointelegraph.com/news/defi-mainstreaming-impossible-until-dexs-integrate-layer-2-experts-say'
    
    
class Sources:
  '''
  source class to define source object
  '''
  def __init__(self,id,name,description,url,category,language):
    self.id = id
    self.name = name
    self.description = description
    self.url = "http://www.afr.com"
    self.category = category
    self.language = language