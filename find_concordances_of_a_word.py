#how to find concordances of a word

import nltk
nltk.download()
from nltk.book import *

print('')
print('''Concodances of the word 'sea' in text 1:''')
print(text1.concordance("sea"))
print('')
