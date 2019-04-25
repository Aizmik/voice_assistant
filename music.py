from os import listdir
import re
import winsound


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
        print('music\\' + song)
        winsound.PlaySound('music\\' + song, winsound.SND_ASYNC |
                           winsound.SND_FILENAME)


def stop():
    winsound.PlaySound(None, winsound.SND_ASYNC)
