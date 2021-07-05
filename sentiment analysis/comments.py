'''In this proyect I'll take a news article of the New York Times to make 
    a sentiment analysis with it, this also could represent how biased is the article. 
    The article in wich will be run the analysis is 
    "Lo que sabemos sobre la acusación formal en contra de la Organización Trump"   
    @author: Santiago Puerta'''


import requests #conecting to AppleStore server
from lxml import html as html #making an html document compatible with XPath
from sentiment import analysis #sentiment analysis
from sentiment import graphs #graphs


#web page where the article is taken of
PAGE = 'https://www.nytimes.com/es/2021/07/03/espanol/organizacion-trump.html'
PARAGRAPHS = '//p[@class = "css-axufdj evys1bk0"]/text()' #Xpath to find the paragraphs


def to_str(paragraphs: list) -> str: #function to make a single string out of a list
    article = ""
    try:
        for line in paragraphs:
            article += line
        return article
    except ValueError as ve:
        print(ve)


def get_article():
    try:
        response = requests.get(PAGE) #response of the Apple Store server
        if response.status_code == 200: #if server gives me an OK
            doc = response.content.decode('utf-8') #the HMTL that is given I'll decode it
            x_doc = html.fromstring(doc) #I'll convert the doc to something that I can control with Xpath
            paragraphs = x_doc.xpath(PARAGRAPHS)
            return paragraphs
        else: #if server gives me an error wich error is?
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    paragraphs = get_article() #get the list of the comments of the app
    article = to_str(paragraphs) #get a single string out of the paragraphs
    ps_tuple = analysis(article) #results from the sentiment analysis
    graphs(ps_tuple[0], ps_tuple[1])


if __name__ == '__main__':
    run()

