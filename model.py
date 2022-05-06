class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,description,urlToImage,content,publishedAt):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt= publishedAt
class Sources:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url):

        self.id= id
        self.name = name
        self.description = description
        self.url = url


            