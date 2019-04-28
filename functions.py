import urllib.request as r
import datetime
import bs4


def get_weather(when=['сейчас'], location=['СанктПетербурге']):
    """ when should be normalized
    """
    dow = {'понедельник': 'Пн', 'вторник': 'Вт', 'среда': 'Ср',
           'четверг': 'Чт', 'пятница': 'Пт', 'суббота': 'Сб',
           'воскресенье': 'Вс', 'завтра': 'завтра', 'сегодня': 'сегодня'}
    city = {'Москве': 'moscow', 'СанктПетербурге': 'saint-petersburg',
            'Петрозаводске': 'petrozavodsk'}

    url = 'https://yandex.ru/pogoda/'

    if location:
        url += city[location[0]]
    else:
        location = ['СанктПетербурге']

    page = r.urlopen(url)
    soup = bs4.BeautifulSoup(page, 'html.parser')

    if not when == ['сейчас'] and when:
        for forecast in soup.select('a.link'):
            day = ''
            cast = bs4.BeautifulSoup(str(forecast), 'html.parser')
            try:
                day = cast.select('div.forecast-briefly__name')[0].text
            except Exception:
                pass

            if day == dow[when[0]]:
                temp = cast.select('div.temp > span.temp__value')[0].text
                condition = cast.select('div.forecast-briefly__condition')[0].text

                return 'В ' + str(location[0]) + ', в ' + day \
                       + ', ' + temp + ', ' + condition

    when = ['сейчас']

    return 'В ' + str(location[0]) + ' ' + str(when[0])\
           + ' ' + str(soup.select('span.temp__value')[0].text)\
           + ', ' + str(soup.select('div.link__condition')[0].text)\
           + ', ' + 'ощущается' + ' ' + 'как' + ' ' + str(soup.select(
                'div.temp > span.temp__value')[1].text)


def get_time():
    return datetime.datetime.now().time()
