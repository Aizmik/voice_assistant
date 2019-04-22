import pickle
from music import play
from functions import get_weather
from functions import get_time
from keyword_finder import find_city
from keyword_finder import find_day
from training_functions import get_bow_vector


with open(r'models\MultinominalNB_model.pkl', 'rb') as m:
    ML_model = pickle.load(m)

previous_params = [None, None]
previous_intent = None
while(True):
    phraze = input()
    intent = ML_model.predict([get_bow_vector(phraze)])

    if intent == 0:
        params = [find_day(phraze), find_city(phraze)]

        if previous_intent == intent:
            if not params[0]:
                params[0] = previous_params[0]
            if not params[1]:
                params[1] = previous_params[1]

        previous_params = params
        previous_intent = intent
        print(get_weather(params[0], params[1]))
    if intent == 1:
        print(get_time())
    if intent == 2:
        play(phraze)
