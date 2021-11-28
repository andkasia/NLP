import nltk

from nltk.corpus import gutenberg
from nltk.corpus import inaugural

gutenberg_file_names = gutenberg.fileids()
print('Names of the files in the Gutenberg corpus:', *gutenberg_file_names)

inaugural_file_names = inaugural.fileids()
print('Names of the files in the Gutenberg corpus:', *inaugural_file_names)