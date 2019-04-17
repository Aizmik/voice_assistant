import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from nltk import word_tokenize
from gensim.models import FastText
import fasttext
import pickle
import pymorphy2
import numpy as np

def get_vector(sentence):

    FT_model = FastText.load(r'models\fasttext.model')
    sentence = word_tokenize(sentence)
    vector = []
    morph = pymorphy2.MorphAnalyzer()

    for word in sentence:
        word = morph.parse(word)[0].normal_form
        try:
            if not vector:
                vector = FT_model[word]
            else:
                vector += FT_model[word]
        except:
            pass

    return vector

def get_bow_vector(sentence):
    morph = pymorphy2.MorphAnalyzer()
    sentence = word_tokenize(sentence)

    with open(r'models\bag_of_words.pickle', 'rb') as f:
        bow = pickle.load(f)


    for word in sentence:
        word = morph.parse(word)[0].normal_form
        try:
            bow[word] += 1
        except:
            if word.isdigit == False: print(word)

    return(np.array(list(bow.values())).astype(float))
