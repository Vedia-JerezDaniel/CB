import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from autocorrect import Speller
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ecb = "DB/rate_ecb"
infile = open(ecb, "rb")
ecb = pickle.load(infile)

ecb.sample(5)

ecb["text"] = ecb["text"].fillna(value="")

Apos_dict={"'s":" is","n't":" not","'m":" am","'ll":" will", "'d":" would","'ve":" have","'re":" are"}
#replace the contractions
for key,value in Apos_dict.items():
    if key in ecb["text"]:
        ecb["text"]=ecb["text"].replace(key,value)

nltk.download('wordnet')
stemmer = WordNetLemmatizer()
stop_words = ['!', ',', '.', '?', '-s', '-ly', '</s> ', 's']
ecb["text"] = [stemmer.lemmatize(word) for word in ecb["text"]]

porter = PorterStemmer()
ecb["text"] = [porter.stem(word) for word in ecb["text"]]

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(['bankers', 'speeches','will', 'central','bank','s','u','uk','co','bis','bi','end', 'see', 'set', 'much', 'even', "bankers'", 'available', 'online','monetary','policy','mario','draghi','view','ecb','claude','trichet','governing','council','eu','president','euro', 'area','union','european','mr','christine','lagarde','per','cent','frankfurt','jean','m','one','us','second','two'])

ecb_w =" ".join(ecb['text']).lower()

def cloud(word_string):
    plt.figure(figsize=(15, 15), facecolor='k', edgecolor='k')
    wc = WordCloud(background_color="gray", stopwords=stopwords,
               max_words=50, max_font_size=150,  width=2000, height=1500)
    wc.generate(word_string)
    plt.imshow(wc.recolor(random_state=17), interpolation="bilinear")
    plt.axis('off')
    plt.show()

cloud(ecb_w)

trichet = ecb["text"][:146]
draghi = ecb["text"][147:393]
lagarde = ecb["text"][394:]

trichet_w = " ".join(trichet).lower()
draghi_w = " ".join(draghi).lower()
lagarde_w = " ".join(lagarde).lower()

cloud(trichet_w)
cloud(draghi_w)
cloud(lagarde_w)
