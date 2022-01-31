with open('r191105.txt', encoding="utf8") as f:
     y1911a = f.read()
with open('r191122.txt', encoding="utf8") as f:
     y1911b = f.read()
with open('r191127.txt', encoding="utf8") as f:
     y1911c = f.read()
with open('r191202.txt', encoding="utf8") as f:
     y1912a = f.read()
with open('r191212.txt', encoding="utf8") as f:
     y1912b = f.read()
with open('r191217.txt', encoding="utf8") as f:
     y1912c = f.read()

with open('r200108.txt', encoding="utf8") as f:
     y2001a = f.read()
with open('r200121.txt', encoding="utf8") as f:
     y2001b= f.read()
with open('r200123.txt', encoding="utf8") as f:
     y2001c = f.read()
with open('r200128.txt', encoding="utf8") as f:
     y2001d = f.read()
with open('r200130.txt', encoding="utf8") as f:
     y2001e = f.read()
with open('r200205.txt', encoding="utf8") as f:
     y2002a = f.read()
with open('r200206.txt', encoding="utf8") as f:
     y2002b = f.read()
with open('r200211.txt', encoding="utf8") as f:
     y2002c = f.read()
with open('r200302.txt', encoding="utf8") as f:
     y2003a = f.read()
with open('r200312.txt', encoding="utf8") as f:
     y2003b = f.read()
with open('r200414.txt', encoding="utf8") as f:
     y2004a = f.read()
with open('r200415.txt', encoding="utf8") as f:
     y2004b = f.read()
with open('r200416.txt', encoding="utf8") as f:
     y2004c = f.read()
with open('r200430.txt', encoding="utf8") as f:
     y2004d = f.read()
with open('r200508.txt', encoding="utf8") as f:
     y2005 = f.read()
with open('r200604.txt', encoding="utf8") as f:
     y2006 = f.read()     

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2019-11-05','2019-11-22','2019-11-27','2019-12-02','2019-12-12','2019-12-17',
'2020-01-08','2020-01-21','2020-01-23','2020-01-28','2020-01-30','2020-02-05','2020-02-06','2020-02-11','2020-03-02','2020-03-12','2020-04-14','2020-04-15','2020-04-16','2020-04-30','2020-05-08','2020-06-04']
df.shape

df['text'] = [y1911a,y1911b,y1911c,y1912a,y1912b,y1912c,
y2001a,y2001b,y2001c,y2001d,y2001e,y2002a,y2002b,y2002c,y2003a,y2003b,y2004a,y2004b,y2004c,y2004d,
y2005,y2006]  
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_lag1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()