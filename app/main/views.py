from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources,get_articles
from ..models import NewsSource, NewsArticle

@main.route('/')
def index():
	'''
	View roote page function that return the index page and its data
	'''

	status_sources = get_sources('sources')

	title='Home - Get the most up to date news on News One'
	return render_template('index.html',title=title, status = status_sources)

@main.route('/news/<news_id>')
def news(news_id):
	'''
	Views news page function that returns news details page and its data
	'''

@main.route('/article/<id>')
def article(id):
	'''
	View articles page function for all the articles for specific source
	'''

	articles_sources = get_articles(id)



	return render_template('news.html', articles = articles_sources)
