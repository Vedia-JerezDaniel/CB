with open('040608.txt', encoding="utf8") as f:
    y0406 = f.read()
with open('070108.txt', encoding="utf8") as f:
    y0701 = f.read()
with open('100108.txt', encoding="utf8") as f:
    y1001 = f.read()
with open('110208.txt', encoding="utf8") as f:
    y1102 = f.read()
with open('120308.txt', encoding="utf8") as f:
    y1203 = f.read()
with open('121108.txt', encoding="utf8") as f:
    y1211 = f.read()
with open('130508.txt', encoding="utf8") as f:
    y1305 = f.read()
with open('131108.txt', encoding="utf8") as f:
    y1311 = f.read()
with open('161008.txt', encoding="utf8") as f:
    y1610 = f.read()
with open('210408.txt', encoding="utf8") as f:
    y2104 = f.read()
with open('220208.txt', encoding="utf8") as f:
    y2202 = f.read()
with open('230208.txt', encoding="utf8") as f:
    y2302 = f.read()
with open('240708.txt', encoding="utf8") as f:
    y2407 = f.read()
with open('250208.txt', encoding="utf8") as f:
    y2502 = f.read()
with open('250908.txt', encoding="utf8") as f:
    y2509 = f.read()
with open('251208.txt', encoding="utf8") as f:
    y2512 = f.read()
with open('260608.txt', encoding="utf8") as f:
    y2606 = f.read()
with open('290908.txt', encoding="utf8") as f:
    y2909 = f.read()
    
import pandas as pd
df = pd.DataFrame()

df['date'] = ['2008-06-04','2008-01-07','2008-01-10','2008-02-11','2008-03-12','2008-11-12','2008-05-13','2008-11-13','2008-10-16','2008-04-21','2008-02-22','2008-02-23','2008-07-24','2008-02-25','2008-09-25','2008-12-25','2008-06-26', '2008-09-29']
df.shape

df['text'] = [y0406, y0701, y1001, y1102, y1203, y1211,y1305, y1311, y1610, y2104, y2202, y2302, y2407, y2502, y2509, y2512, y2606, y2909]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_fuk'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()