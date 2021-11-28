#how to find common dictiory for sentences and a common dictionary for all the sentences

import nltk
nltk.download()
from nltk.book import *

slowniki = []
wspolny_slownik = set()
for sent in [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9]:
    slowniki.append(sorted(set(sent)))
    wspolny_slownik = wspolny_slownik.union(set(sent))

wspolny_slownik = sorted(wspolny_slownik, key = str.lower)

for index, slownik in enumerate(slowniki):
    print('sent' + str(index + 1), slownik)

print('wszystkie słowniki', wspolny_slownik)