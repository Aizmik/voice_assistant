import json
import pickle
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import FastText
from nltk.tokenize import RegexpTokenizer


def data():
    tokenizer = RegexpTokenizer(r'[а-я]+')
    with open(r'data\bash_org.json', 'r') as file:
        data = json.load(file)

    corpus = []
    for phraze in data:
        corpus.append(tokenizer.tokenize(phraze['text'].lower()))
           
    return corpus


def train_fasttext(corpus):
    model = FastText(size=9, window=2, min_count=1)
    model.build_vocab(sentences=corpus)
    model.train(sentences=corpus, total_examples=len(corpus), epochs=10)

    model.save(r'models\fasttext.model')


def train_bow(corpus):
    bag = {}
    for sentence in corpus:
        for word in sentence:
            if word not in bag.keys():
                bag[word] = 0 

    with open(r'models\bag_of_words.pickle', 'wb') as f:
        pickle.dump(bag, f)


train_bow(data())
