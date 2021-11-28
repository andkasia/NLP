#how to calculate vocabulary size

import nltk
nltk.download()
from nltk.book import *


def vocab_size(text):
    words = set()
    for token in text.tokens:
        if str.isalpha(token):
            words.add(str.lower(token))

    return len(words)

for index, text in enumerate([text1, text2, text3, text4, text5, text6, text7, text8, text9]):
    print('W tekście ' + str(index + 1) + ' słownictwo wynosi:', vocab_size(text))