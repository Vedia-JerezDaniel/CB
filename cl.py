# load text
filename = 'data//BOE//Carney_clean.txt'
file = open(filename, 'rt',encoding="mbcs")
text = file.read()
file.close()
text

# split into words by white space
words = text.split()
print(words[:100])

## 3. Select Words
# split based on words only
import re
words = re.split(r'\W+', text)
print(words[:100])

## . Split by Whitespace and Remove Punctuation
import string
print(string.punctuation)
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:100])


words = [word.lower() for word in words]
print(words[:100])




import nltk
nltk.download()

from nltk import sent_tokenize
sentences = sent_tokenize(text)
print(sentences[0])

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# print(tokens[:100])

#  Filter Out Punctuation
words = [word for word in tokens if word.isalpha()]
print(words[:100])

# Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
# print(stop_words)
words = [w for w in words if not w in stop_words]
print(words[:100])

# Stem Words
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]
print(stemmed[:100])


## gEEk 
tweet = re.sub(r'https?:\/\/.\S+', "", text)
tweet = re.sub(r'\n', ' ', tweet)
tweet[:100]


tx=text.split('\n')
tx[:100]
