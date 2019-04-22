from os import listdir
import re
from playsound import playsound


def get_song(singer):
    songs = []
    for song in listdir('music'):
        if singer in song:
            songs.append(song)
    return songs


def get_singer(sentence):
    return re.search('^(Сыграй ка мне |Включи |Хочу послушать )(.+)',
                     sentence).group(2)


def play(sentence):
    for song in get_song(get_singer(sentence)):
        playsound('music\\' + song)
