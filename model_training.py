import pickle
import numpy as np
import pandas as pd
from nltk import word_tokenize
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from sklearn.naive_bayes import GaussianNB
from gensim.models import FastText


model = FastText.load('fasttext.model')

clf = GaussianNB()

data = pd.read_excel('intents.xlsx')
data['question'] = data['question'].apply(lambda x: word_tokenize(x))
X = []
for quest in data['question']:
    vector = model[quest[0]]
    for word in quest[:0]:
        vector *= model[word]
    X.append(vector)
        

y = np.array(data['class'])

X = np.array(X)

clf.fit(X,y)

with open('GaussianNB_model.pkl', 'wb') as fid:
    pickle.dump(clf, fid)  