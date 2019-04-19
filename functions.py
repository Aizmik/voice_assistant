import urllib.request as r
import datetime
import bs4


def get_weather(when=['сейчас'], location=['СанктПетербурге']):
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

    if not when == ['сейчас']:
        for forecast in soup.select('a.link'):
            try:
                cast = bs4.BeautifulSoup(str(forecast), 'html.parser')
                day = cast.select('div.forecast-briefly__name')[0].text
                if day == dow[when]:
                    temp = cast.select('div.temp > span.temp__value')[0].text
                    condition = cast.select('div.forecast-briefly__condition')[0].text

                    return 'В ' + str(location[0]) + ' ' + str(when)\
                           + ', ' + temp + ', ' + condition
            except(Exception):
                pass

    when = ['сейчас']
    if not location:
        location = ['СанктПетербурге']
    return 'В ' + str(location[0]) + ' ' + str(when[0])\
           + ' ' + str(soup.select('span.temp__value')[0].text)\
           + ', ' + str(soup.select('div.link__condition')[0].text)\
           + ', ' + 'ощущается' + ' ' + 'как' + ' ' + str(soup.select(
                'div.temp > span.temp__value')[1].text)


def get_time():
    return datetime.datetime.now().time()
