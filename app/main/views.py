from flask import render_template
from .import main

@main.route('/')
def index():
	'''
	Return index page and its data
	'''

	# news_headlines = get_headlines()
	title = 'New Highlight- Fast and reliable way to get news'
	return render_template('index.html',title = title, headlines = news_headlines)