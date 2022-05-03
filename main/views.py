from typing import _get_type_hints_obj_allowed_types
from flask import render_template
from.import main
from ..request import get_news

#views
@main.route('/')
def index():

    news=get_news()
    title = 'galaxynews'
    return render_template('index.html', title = title,articles =news)
    

