'''In this proyect I'll take some comments from
    Facebook.com for making a sentiment analysis
    with them.'''


import requests
from lxml import html as html


#web page where the article is taken of
PAGE = "https://www.semana.com/nacion/articulo/gustavo-petro-basta-ya-editorial-de-semana/202139/"
COMMENTS = '//p[@class = "section sp-8"]/text()' #Xpath to find the atricle information


def get_comments():
    try:
        response = requests.get(PAGE) #response of the facebook server
        if response.status_code == 200: #if server gives me an OK
            doc = response.content.decode('utf-8') #the HMTL that is given i'll decode it
            x_doc = html.fromstring(doc)#I'll convert the doc to something that I can control with Xpath
            comments = x_doc.xpath(COMMENTS)
            print(comments)
        else: #if server gives me an error wich eror is?
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    get_comments()


if __name__ == '__main__':
    run()

