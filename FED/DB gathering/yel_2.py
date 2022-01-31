with open('r160928.txt', encoding="utf8") as f:
     y1609 = f.read()
with open('r161003.txt', encoding="utf8") as f:
     y1610a = f.read()
with open('r161017.txt', encoding="utf8") as f:
     y1610b = f.read()
with open('r161124.txt', encoding="utf8") as f:
     y1611 = f.read()
with open('r161220.txt', encoding="utf8") as f:
     y1612 = f.read()
with open('r170116.txt', encoding="utf8") as f:
     y1701a = f.read()
with open('r170119.txt', encoding="utf8") as f:
     y1701b = f.read()
with open('r170120.txt', encoding="utf8") as f:
     y1701c = f.read()
with open('r170216.txt', encoding="utf8") as f:
     y1702 = f.read()
with open('r170313.txt', encoding="utf8") as f:
     y1703a = f.read()
with open('r170324.txt', encoding="utf8") as f:
     y1703b = f.read()
with open('r170329.txt', encoding="utf8") as f:
     y1703c = f.read()
with open('r170508.txt', encoding="utf8") as f:
     y1705 = f.read()
with open('r170721.txt', encoding="utf8") as f:
     y1707 = f.read()
with open('r170829.txt', encoding="utf8") as f:
     y1708 = f.read()
with open('r171012.txt', encoding="utf8") as f:
     y1710a = f.read()
with open('r171013.txt', encoding="utf8") as f:
     y1710b = f.read()
with open('r171017.txt', encoding="utf8") as f:
     y1710c = f.read()
with open('r171024.txt', encoding="utf8") as f:
     y1710d = f.read()
with open('r171222.txt', encoding="utf8") as f:
     y1712 = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2016-09-27','2016-10-08','2016-10-17','2016-11-03','2016-12-12',
'2017-01-16','2017-01-19','2017-01-20','2017-02-14','2017-03-07','2017-03-24','2017-03-29','2017-05-08','2017-07-21','2017-08-29','2017-10-12','2017-10-13','2017-10-17','2017-10-24','2017-12-22']
df.shape

df['text'] = [y1609,y1610a,y1610b,y1611,y1612,
y1701a,y1701b,y1701c,y1702,y1703a,y1703b,y1703c,y1705,y1707,y1708,y1710a,y1710b,y1710c,y1710d,y1712]  
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_yel2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()