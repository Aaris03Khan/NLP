from pandas import DataFrame
from nltk.tokenize import sent_tokenize, word_tokenize
text=["Hello it's me.      . Strings are sequences of characters.",
("Hello it's me. yasaswi it is     . Strings are sequences of characters."),
("Hello it's me.   aaris it is   . Strings are sequences of characters."),
("Hello it's me.   Mythri it is   . Strings are sequences of characters."),
("Hello it's me.   Pooh it is   . Strings are sequences of characters.")]
C = {1: text }
df = DataFrame(C, columns= [1])
export_csv = df.to_csv (r'G:\NLP\abstract.csv', index = None, header=True) # here you have to write path, where result file will be stored
