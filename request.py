import urllib.request,json
from .model import News
#getting api key
api_key =None
#getting the news base url
base_url = None
def configure_request(app):
    global api_key,base_url
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_API_BASE_URL']

    def get_news():
        '''
        function that gets the json response to our url request
        '''
        get_news_url = base_url.format(api_key)

        