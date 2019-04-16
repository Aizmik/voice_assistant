import pickle
import numpy as np
import pandas as pd
from nltk import word_tokenize
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from sklearn.naive_bayes import GaussianNB
from gensim.models import FastText
from training_functions import get_bow_vector


clf = GaussianNB()

data = pd.read_excel(r'data\intents.xlsx')
X = []


for quest in data['question']:
    X.append(get_bow_vector(quest))
        

y = np.array(data['class'])
X = np.array(X)
clf.fit(X,y)


with open(r'models\GaussianNB_model.pkl', 'wb') as fid:
    pickle.dump(clf, fid)  