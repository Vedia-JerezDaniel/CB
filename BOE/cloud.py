import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
#from autocorrect import Speller
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

boe = "DB/rate_boe"
infile = open(boe, "rb")
boe = pickle.load(infile)

boe.sample(5)

boe["text"] = boe["text"].fillna(value="")

Apos_dict={"'s":" is","n't":" not","'m":" am","'ll":" will", "'d":" would","'ve":" have","'re":" are"}
#replace the contractions
for key,value in Apos_dict.items():
    if key in boe["text"]:
        boe["text"]=boe["text"].replace(key,value)

nltk.download('wordnet')
stemmer = WordNetLemmatizer()
stop_words = ['!', ',', '.', '?', '-s', '-ly', '</s> ', 's']
boe["text"] = [stemmer.lemmatize(word) for word in boe["text"]]

porter = PorterStemmer()
boe["text"] = [porter.stem(word) for word in boe["text"]]

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(['bankofengland','bankers', 'speeches','will', 'central','bank','s','u','uk','co','bis','bi','end', 'see', 'set', 'much', 'even', 'boe_pressoffice', 'available', 'online', 'andrew', 'bailey','mpc','england'])

def cloud(word_string):
    plt.figure(figsize=(15, 15), facecolor='k', edgecolor='k')
    wc = WordCloud(background_color="gray", stopwords=stopwords,
               max_words=50, max_font_size=150,  width=2000, height=1500)
    wc.generate(word_string)
    plt.imshow(wc.recolor(random_state=17), interpolation="bilinear")
    plt.show()
    
boe_w =" ".join(boe['text']).lower()
cloud(boe_w)  

king = boe["text"][:23]
carney = boe["text"][23:106]
bailey = boe["text"][106:]

king_w = " ".join(king).lower()
carney_w = " ".join(carney).lower()
bailey_w = " ".join(bailey).lower()

cloud(king_w)
cloud(carney_w)
cloud(bailey_w)
