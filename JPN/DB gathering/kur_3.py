with open('171106.txt', encoding="utf8") as f:
    y1711a = f.read()
with open('171116.txt', encoding="utf8") as f:
    y1711b = f.read()
with open('171205.txt', encoding="utf8") as f:
    y1712a = f.read()
with open('171211.txt', encoding="utf8") as f:
    y1712b = f.read()
with open('171229.txt', encoding="utf8") as f:
    y1712c = f.read()

with open('180112.txt', encoding="utf8") as f:
    y1801 = f.read()
with open('180605.txt', encoding="utf8") as f:
    y1806 = f.read()
with open('180903.txt', encoding="utf8") as f:
    y1809a = f.read()
with open('180926.txt', encoding="utf8") as f:
    y1809b = f.read()
with open('181016.txt', encoding="utf8") as f:
    y1810 = f.read()
with open('181105.txt', encoding="utf8") as f:
    y1811a = f.read()
with open('181120.txt', encoding="utf8") as f:
    y1811b = f.read()
with open('181206.txt', encoding="utf8") as f:
    y1812 = f.read()

with open('190107.txt', encoding="utf8") as f:
     y1901a = f.read()
with open('190117.txt', encoding="utf8") as f:
     y1901b = f.read()
with open('190503.txt', encoding="utf8") as f:
     y1905a = f.read()
with open('190513.txt', encoding="utf8") as f:
     y1905b = f.read()
with open('190517.txt', encoding="utf8") as f:
     y1905c = f.read()
with open('190527.txt', encoding="utf8") as f:
     y1905d = f.read()
with open('190529.txt', encoding="utf8") as f:
     y1905e = f.read()
with open('190606.txt', encoding="utf8") as f:
     y1906a = f.read()
with open('190607.txt', encoding="utf8") as f:
     y1906b = f.read()
with open('190612.txt', encoding="utf8") as f:
     y1906c = f.read()
with open('190729.txt', encoding="utf8") as f:
     y1907 = f.read()
with open('190904.txt', encoding="utf8") as f:
     y1909a = f.read()
with open('190925.txt', encoding="utf8") as f:
     y1909b = f.read()
with open('191021.txt', encoding="utf8") as f:
     y1910 = f.read()
with open('191105.txt', encoding="utf8") as f:
     y1911a = f.read()
with open('191128.txt', encoding="utf8") as f:
     y1911b = f.read()
with open('191204.txt', encoding="utf8") as f:
     y1912a = f.read()
with open('191213.txt', encoding="utf8") as f:
     y1912b = f.read()
with open('191227.txt', encoding="utf8") as f:
     y1912c = f.read()

with open('200514.txt', encoding="utf8") as f:
     y2005a = f.read()
with open('200526.txt', encoding="utf8") as f:
     y2005b = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2017-11-06','2017-11-16','2017-12-05','2017-12-11','2017-12-29',
'2018-01-20','2018-06-05','2018-09-05','2018-09-25','2018-10-16','2018-11-09','2018-11-20','2018-12-06',
'2019-01-17','2019-01-17','2019-05-03','2019-05-13','2019-05-17','2019-05-27','2019-05-29','2019-06-06','2019-06-07','2019-06-12','2019-07-13','2019-09-04','2019-09-25','2019-10-21','2019-11-05','2019-11-28','2019-12-04','2019-12-13','2019-12-27',
'2020-05-14','2020-05-26']
df.shape

df['text'] = [y1711a,y1711b,y1712a,y1712b,y1712c,
y1801,y1806,y1809a,y1809b,y1810,y1811a,y1811b,y1812,
y1901a,y1901b,y1905a,y1905b,y1905c,y1905d,y1905e,y1905b,y1906a,y1906b,y1906c,y1907,y1909a,y1909b,y1910,y1911a,y1911b,y1912a,y1912b,
y2005a,y2005b]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_kur3'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()