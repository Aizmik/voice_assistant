import re
import time
import urllib
import database_things
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_comments(url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
    

        keywords = ''
        for tag in soup.select('div.story__tags > a'):
            keywords += tag.text + ' '

        key_id = database_things.insert_keyword(keywords)

        
        par_comments = [soup.select('h1.story__title > span')[0].text]
        chi_comments = []
        for comment in soup.select('div.comment__content > p'):
            chi_comments.append(comment.text)
            par_comments.append(comment.text)


        

        for par, chi in zip(par_comments, chi_comments):
            database_things.insert_phrase(par, chi, key_id)


        time.sleep(5)


def run(url):
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        for theme_url in soup.select('h2.story__title > a'):
            get_comments(theme_url['href'])


    except Exception as e:
        print(e)

