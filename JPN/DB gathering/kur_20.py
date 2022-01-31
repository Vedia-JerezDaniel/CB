with open('r210316.txt', encoding="utf8") as f:
     y2103 = f.read()
with open('r210326.txt', encoding="utf8") as f:
     y2103a = f.read()
with open('r210330.txt', encoding="utf8") as f:
     y2103b = f.read()
with open('r210517.txt', encoding="utf8") as f:
     y2105 = f.read()
with open('r210519.txt', encoding="utf8") as f:
     y2105a = f.read()
with open('r210607.txt', encoding="utf8") as f:
     y2106 = f.read()   
with open('r210804.txt', encoding="utf8") as f:
     y2108 = f.read() 
with open('r210928.txt', encoding="utf8") as f:
     y2109 = f.read()
with open('r211008.txt', encoding="utf8") as f:
     y2110 = f.read()
with open('r211130.txt', encoding="utf8") as f:
     y2111 = f.read()
with open('r211130a.txt', encoding="utf8") as f:
     y2111a = f.read()
with open('r211130b.txt', encoding="utf8") as f:
     y2111b = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2021-03-16','2021-03-23','2021-03-30','2021-05-17','2021-05-19','2021-06-07','2021-08-04',
              '2021-09-28','2021-10-08','2021-11-19','2021-11-27','2021-11-30']
df.shape

df['text'] = [y2103,y2103a,y2103b,y2105,y2105a,y2106,y2108,y2109,y2110,y2111,y2111a,y2111b]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_kur20'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()