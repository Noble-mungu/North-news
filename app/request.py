import urllib .request,json
from .models import Headlines,source

api_key = None

headline_base_url = None
everything_base_url = None
source_base_url = None
source_article_base_url = None
def configure_request(app):
        global api_key, headlines_base_url, everything_base_url, sources_base_url, sources_article_base_url
        api_key = '3cb6f94391e348d6a9b7dcd4dba81826'
        print(api_key)
        headlines_base_url = app.config["HEADLINES_API_BASE_URL"]
        print(headlines_base_url.format(api_key))
        everything_base_url = app.config["EVERYTHING_API_BASE_URL"]
        sources_base_url = app.config["SOURCES_API_BASE_URL"]
        sources_article_base_url = app.config["SOURCES_ARTICLE_API_BASE_URL"]




