import json
import warnings
from gensim.models import FastText
from gensim.test.utils import get_tmpfile
from nltk.tokenize import RegexpTokenizer
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')


def data():
    tokenizer = RegexpTokenizer(r'[А-Яа-я]+')

    with open(r'data\bash_org.json', 'r') as file:
        data = json.load(file)

    corpus = []
    for phraze in data:
        corpus.append(tokenizer.tokenize(phraze['text']))
           
    return corpus

data = data()



model = FastText(size=9, window=2, min_count=1)
model.build_vocab(sentences=data)
model.train(sentences=data, total_examples=len(data), epochs=10)

model.save(r'models\fasttext.model')

