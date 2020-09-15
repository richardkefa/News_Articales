class Articles:
  '''
  News class to define news object
  '''
  def __init__(self,id,author,title,image,publishedate,fullarticle,description):
    
    self.id = id
    self.author = author
    self.title = title
    self.description = description
    self.image = image
    self.publishedate = publishedate
    self.fullarticle = fullarticle
    
    
class Sources:
  '''
  source class to define source object
  '''
  def __init__(self,id,name,description,url,category,language):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language