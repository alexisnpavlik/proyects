'''In this proyect I'll take a news from
    El Espectador for making a sentiment analysis
    using the library textblob.'''


import requests
from lxml import html as html
from sentiment import analysis


#web page where the article is taken of
PAGE = 'https://www.elespectador.com/politica/lgbtfobia-en-la-politica-una-campana-que-visibiliza-la-discriminacion/'
ARTICLE = '//p[@class = "font--secondary"]/text()' #Xpath to find the atricle information


def to_str(article): #function to pass a list to a single string
    news = ""
    for word in article:
        news+= word
    return news


def get_comments():
    try:
        response = requests.get(PAGE) #response of the El Espectador server
        if response.status_code == 200: #if server gives me an OK
            doc = response.content.decode('utf-8') #the HMTL that is given I'll decode it
            x_doc = html.fromstring(doc) #I'll convert the doc to something that I can control with Xpath
            article = x_doc.xpath(ARTICLE)
            return article
        else: #if server gives me an error wich error is?
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    article = get_comments() #Get the list of the paragraphs of the article
    news = to_str(article) #Get a single string out of the paragraphs
    analysis(news) #Results from the sentiment analysis


if __name__ == '__main__':
    run()

