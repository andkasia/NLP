#how to find the longest word in texts

import nltk
nltk.download()
from nltk.book import *

for index, text in enumerate([text1, text2, text3, text4, text5, text6]):
    maxlen = max(len(word) for word in text if str.isalpha(word))
    najdluzsze_slowo= [word for word in text if len(word) == maxlen]

    print('Najdłuższe słowo lub najdłuższe słowa w tekście numer ' + str(index + 1) + ' to:', *najdluzsze_slowo)