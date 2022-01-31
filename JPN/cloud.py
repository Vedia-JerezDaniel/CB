import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from autocorrect import Speller
import nltk
#import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

jpn = "DB/rate_jpn"
infile = open(jpn, "rb")
jpn = pickle.load(infile)

jpn.sample(5)

jpn["text"] = jpn["text"].fillna(value="")

Apos_dict={"'s":" is","n't":" not","'m":" am","'ll":" will", "'d":" would","'ve":" have","'re":" are"}
#replace the contractions
for key,value in Apos_dict.items():
    if key in jpn["text"]:
        jpn["text"]=jpn["text"].replace(key,value)

nltk.download('wordnet')
stemmer = WordNetLemmatizer()
stop_words = ['!', ',', '.', '?', '-s', '-ly', '</s> ', 's']
jpn["text"] = [stemmer.lemmatize(word) for word in jpn["text"]]

porter = PorterStemmer()
jpn["text"] = [porter.stem(word) for word in jpn["text"]]

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(['bankers', 'speeches','will', 'central','bank','s','u','uk','co','bis','bi','end', 'see', 'set', 'much', 'even', "bankers'", 'available', 'online','monetary','policy','japan','percent','regard','chart','given','although','many','due','us','one','second'])

jpn_w =" ".join(jpn['text']).lower()

def cloud(word_string):
    plt.figure(figsize=(15, 15), facecolor='k', edgecolor='k')
    wc = WordCloud(background_color="gray", stopwords=stopwords,
               max_words=50, max_font_size=150,  width=2000, height=1500)
    wc.generate(word_string)
    plt.imshow(wc.recolor(random_state=17), interpolation="bilinear")
    plt.axis('off')
    plt.show()

cloud(jpn_w)

fuk = jpn["text"][:7]
shira = jpn["text"][8:99]
kuroda = jpn["text"][100:]

fuk_w = " ".join(fuk).lower()
shira_w = " ".join(shira).lower()
kuroda_w = " ".join(kuroda).lower()

cloud(fuk_w)
cloud(shira_w)
cloud(kuroda_w)

