#how to find most common words in a text

import nltk
nltk.download()
from nltk.book import *

słowa = []
for token in text1.tokens:
    if str.isalpha(token):
        słowa.append(str.lower(token))

najczestsze_słowa = FreqDist(słowa)

print('10 najczęściej występujących słów w tekście 1 oraz ilość ich wystąpień:' , *najczestsze_słowa.most_common(10))