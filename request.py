from tkinter import NONE
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

        with urllib.request.urlopen(get_news_url)as url:
            get_news_data = url.read()
            get_news_response = json.loads(get_news_data)

            news_results =NONE

            if get_news_response['articles']:
                news_results_list = get_news_response['articles']

                #print(news_results_list)
                news_results=process_results(news_results_list)

                return news_results
    def process_results(news_list):

        news_results =[]
        for news_item in news_list:
            title = news_item.get('title')
            description = news_item.get('description')
            urlToImage = news_item.get('urlToImage')
            content = news_item.get('content')
            publishedAt = news_item.get('publishedAt')

            news_object = News(title,description,urlToImage,content,publishedAt)
            news_results.append(news_object)

            return news_results