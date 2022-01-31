with open('r190606.txt', encoding="utf8") as f:
     y1906a = f.read()
with open('r190613.txt', encoding="utf8") as f:
     y1906b = f.read()
with open('r190618.txt', encoding="utf8") as f:
     y1906c = f.read()
with open('r190729.txt', encoding="utf8") as f:
     y1907 = f.read()
with open('r190912.txt', encoding="utf8") as f:
     y1909a = f.read()
with open('r190924.txt', encoding="utf8") as f:
     y1909b = f.read()
with open('r190926.txt', encoding="utf8") as f:
     y1909c = f.read()     
with open('r191002.txt', encoding="utf8") as f:
     y1910a = f.read()
with open('r191011.txt', encoding="utf8") as f:
     y1910b = f.read()
with open('r191018.txt', encoding="utf8") as f:
     y1910c = f.read()
with open('r191024.txt', encoding="utf8") as f:
     y1910d = f.read()
with open('r191028.txt', encoding="utf8") as f:
     y1910e = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2019-06-06','2019-06-13','2019-06-18','2019-07-21','2019-09-12','2019-09-21',
'2019-09-26','2019-10-02','2019-10-11','2019-10-18','2019-10-24','2019-10-28']
df.shape

df['text'] = [
y1906a,y1906b,y1906c,y1907,y1909a,y1909b,y1909c,y1910a,y1910b,y1910c,y1910d,y1910e]  
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_dra7'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()