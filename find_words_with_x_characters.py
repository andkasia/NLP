#how to find words that have x characters, at the example of 4 characters

import nltk
nltk.download()
from nltk.book import *

slowo_4_literowe = set()
for token in text1.tokens:
    if len(token) == 4 and str.isalpha(token):
        slowo_4_literowe.add(token)

slowa_4_literowe_alfabetycznie = sorted(slowo_4_literowe, key=str.lower)

print('Słowa 4-literowe w tekście 1:', *slowa_4_literowe_alfabetycznie)
print('Liczba słów 4-literowych w tekście 1:', len(slowo_4_literowe))