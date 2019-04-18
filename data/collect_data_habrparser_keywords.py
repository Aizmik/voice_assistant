import urllib.request as r
import re
from bs4 import BeautifulSoup


def get_keywords(url, page_number):
    try:
        page = r.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        titles = []
        for title in soup.select('h2.post__title > a'):
            titles.append(title.text)

        keywords = []
        for ul in soup.select('ul.post__hubs'):
            keys = re.findall(r'>([A-ZА-Я]\w*[ *\w|\S*]*)</a>', str(ul))
            keywords.append(keys.copy())

        with open('data.txt', 'a', encoding='utf-8') as f:
            for title in titles:
                for key in keywords[0]:
                    f.write(title + '\t' + key + '\n')
                keywords.pop(0)

        page_number += 1
        get_keywords('https://habr.com/ru/all/page' + str(page_number), page_number)

    except Exception as e:
        print(e)


get_keywords('https://habr.com/ru/all/', 1)
