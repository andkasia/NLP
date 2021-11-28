#calculate the lexical diversity of texts

import nltk
nltk.download()
from nltk.book import *

def compute(text):
    liczba_slow = len(text)
    slowa_rozne = len(set(text))
    lexical_diversity = float(liczba_slow) / float(slowa_rozne)

    return (liczba_slow, slowa_rozne, lexical_diversity)


print('---------------------------------------------------------')
print('| tekst | liczba słow | słowa różne | lexical diversity |')
print('---------------------------------------------------------')

wszystkie_teksty = {
    'text1': text1,
    'text2': text2,
    'text3': text3,
    'text4': text4,
    'text5': text5,
    'text6': text6,
    'text7': text7,
    'text8': text8,
    'text9': text9,
}

for key in wszystkie_teksty.keys():
    text = wszystkie_teksty[key][0]
    words = wszystkie_teksty[key][1]

    liczba_slow, slowa_rozne, lexical_diversity = compute(text)

    print('|', key.ljust(5, ' '), '|', str(liczba_slow).ljust(11, ' '), '|', str(slowa_rozne).ljust(11, ' '), '|', ('%.2f' % lexical_diversity).ljust(17, ' '), '|')

print('---------------------------------------------------------')