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

def get_headlines():
    '''
    Gets the json response to our url request
    '''
    get_headlines_url = headlines_base_url.format(api_key)
    print(get_headlines_url)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_results(headlines_results_list)

    return headlines_results
def get_sources(category):
        '''
        Gets the json response to our url request
        '''
        get_sources_url = sources_base_url.format(category, api_key)

        with urllib.request.urlopen(get_sources_url) as url:
                get_sources_data = url.read()
                get_sources_response = json.loads(get_sources_data)

                sources_results = None

                if get_sources_response['sources']:
                        sources_results_list = get_sources_response['sources']
                        sources_results = process_sources(sources_results_list)

        return sources_results

def process_sources(sources):
        """
        Process list of sources and returns list of source objects
        """
        source_results = []
        
        for source in sources:
                id = source.get("id")
                name = source.get("name")
                description = source.get("description")
                url = source.get("url")
                category = source.get("category")
                language = source.get("language")
                country = source.get("country")

                if description:
                        new_source = Sources(id, name, description, url, category, language, country)
                        source_results.append(new_source)
        return source_results

def get_sources_articles(id):

        get_sources_article_url = sources_article_base_url.format(id,api_key)

        with urllib.request.urlopen(get_headlines_url) as url:
                get_headlines_data = url.read()
                get_headlines_response = json.loads(get_headlines_data)

                headlines_results = None

                if get_headlines_response['articles']:
                        headlines_results_list = get_headlines_response['articles']
                        headlines_results = process_results(headlines_results_list)

        return headlines_results

