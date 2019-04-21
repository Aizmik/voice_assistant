import urllib.request as r
import re
from bs4 import BeautifulSoup
import pandas as pd


def get_keywords(url, page_number, df=None, i=None):
    try:
        page = r.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        titles = []
        for title in soup.select('h2.post__title > a'):
            titles.append(title.text)

        keywords = []
        for ul in soup.select('ul.post__hubs'):
            keys = re.findall(r'>([A-ZА-Я]\w*[ *\w|\S*]*)</a>', str(ul))
            keywords.append(','.join(keys))

        for title, key in zip(titles, keywords):
            print(f'{title} - {key}')
            interested = input()
            df.loc[i] = [title, key, interested]
            i += 1

        page_number += 1

        page_url = 'https://habr.com/ru/all/page' + str(page_number)
        df.to_csv('my_rates.csv', encoding='UTF-8', index=False)
        get_keywords(page_url, page_number, df, i)

    except Exception as e:
        print(e)


df = pd.DataFrame(columns=['title', 'keys', 'target'])
i = 0

get_keywords('https://habr.com/ru/all/', 1, df, i)
