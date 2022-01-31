import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from autocorrect import Speller
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

fed = "DB/rate_fed"
infile = open(fed, "rb")
fed = pickle.load(infile)

fed.sample(5)

fed["text"] = fed["text"].fillna(value="")

Apos_dict={"'s":" is","n't":" not","'m":" am","'ll":" will", "'d":" would","'ve":" have","'re":" are"}
#replace the contractions
for key,value in Apos_dict.items():
    if key in fed["text"]:
        fed["text"]=fed["text"].replace(key,value)

nltk.download('wordnet')
stemmer = WordNetLemmatizer()
stop_words = ['!', ',', '.', '?', '-s', '-ly', '</s> ', 's']
fed["text"] = [stemmer.lemmatize(word) for word in fed["text"]]

porter = PorterStemmer()
fed["text"] = [porter.stem(word) for word in fed["text"]]

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(['bankers', 'speeches','will', 'federal','reserve','s','u','co','bis','bi','end', 'see', 'set', 'much', 'even', "bankers'", 'available', 'online','monetary','policy','view','fed','governing','council','president','percent','united','states','committee','fomc','although','ben','l','janet','yellen','pdf','federalreserve', 'gov','governor','jerome','h','us','one','second'])

fed_w =" ".join(fed['text']).lower()

def cloud(word_string):
    plt.figure(figsize=(15, 15), facecolor='k', edgecolor='k')
    wc = WordCloud(background_color="gray", stopwords=stopwords,
               max_words=50, max_font_size=150,  width=2000, height=1500)
    wc.generate(word_string)
    plt.imshow(wc.recolor(random_state=17), interpolation="bilinear")
    plt.axis('off')
    plt.show()

cloud(fed_w)

bernanke = fed["text"][:147]
yellen = fed["text"][148:202]
powell = fed["text"][202:]

bernanke_w = " ".join(bernanke).lower()
yellen_w = " ".join(yellen).lower()
powell_w = " ".join(powell).lower()

cloud(bernanke_w)
cloud(yellen_w)
cloud(powell_w)


