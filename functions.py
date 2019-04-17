import urllib.request as r
import datetime
import bs4


def get_weather(when=None, location='СанктПетербурге'):
    """ when should be normalized
    """
    dow = {'Понедельник': 'Пн', 'Вторник': 'Вт', 'Среда': 'Ср', 'Четверг': 'Чт',
           'Пятница': 'Пт', 'Суббота': 'Сб', 'Воскресенье': 'Вс'}
    city = {'Москве': 'moscow', 'СанктПетербурге': 'saint-petersburg',
            'Петрозаводске': 'petrozavodsk'}

    url = 'https://yandex.ru/pogoda/'

    if location:
        url += city[location[0]]

    page = r.urlopen(url)
    soup = bs4.BeautifulSoup(page, 'html.parser')

    if when:
        for forecast in soup.select('a.link'):
            try:
                cast = bs4.BeautifulSoup(str(forecast), 'html.parser')
                if cast.select('div.forecast-briefly__name')[0].text == dow[when]:
                    return[cast.select('div.temp > span.temp__value')[0].text,
                           cast.select('div.forecast-briefly__condition')[0].text]
            except(Exception):
                pass

    return [soup.select('span.temp__value')[0].text,
            soup.select('div.link__condition')[0].text,
            soup.select('div.temp > span.temp__value')[1].text]


def get_time():
    return datetime.datetime.now()
