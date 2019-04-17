import nltk
import pymorphy2


def find_city(sentence):
    morph = pymorphy2.MorphAnalyzer()
    cities = []

    for word in nltk.word_tokenize(sentence):
        tags = str(morph.parse(word)[0].tag)

        if 'Geox sing' in tags:
            cities.append(word)

    return cities


def find_day(sentence):
    morph = pymorphy2.MorphAnalyzer()
    possible_tags = [
        'ADVB', 'NOUN,inan,femn sing,accs', 'NOUN,inan,masc sing,accs']
    times = []

    for word in nltk.word_tokenize(sentence):
        tags = str(morph.parse(word)[0].tag)

        if tags in possible_tags:
            times.append(word)

    return times
