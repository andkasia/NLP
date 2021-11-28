#find words with more than x characters

import nltk
nltk.download()
from nltk.book import *

slowo_wiecej_niz_17 = set()
for token in text1.tokens:
    if len(token) > 17 and str.isalpha(token):
        slowo_wiecej_niz_17.add(token)

slowa_wiecej_niz_17_alfabetycznie = sorted(slowo_wiecej_niz_17, key=str.lower)

print('Słowa w tekście 1, które zawierają więcej niż 17 liter:', *slowa_wiecej_niz_17_alfabetycznie)
print('Liczba słów w tekście 1, które zawierają więcej niż 17 liter:', len(slowo_wiecej_niz_17))