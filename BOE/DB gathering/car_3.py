### CARNEY ONE SPEECHES

with open('r180420.txt', encoding="utf8") as f:
     y1804 = f.read()
with open('r180514.txt', encoding="utf8") as f:
     y1805a = f.read()
with open('r180528.txt', encoding="utf8") as f:
     y1805b = f.read()
with open('r180611.txt', encoding="utf8") as f:
     y1806a = f.read()
with open('r180627.txt', encoding="utf8") as f:
     y1806b = f.read()
with open('r180724.txt', encoding="utf8") as f:
     y1807 = f.read()
with open('r180914.txt', encoding="utf8") as f:
     y1809 = f.read()
with open('r181025.txt', encoding="utf8") as f:
     y1810 = f.read()
with open('r181105.txt', encoding="utf8") as f:
     y1811a = f.read()
with open('r181122.txt', encoding="utf8") as f:
     y1811b = f.read()

with open('r190212.txt', encoding="utf8") as f:
     y1902 = f.read()
with open('r190322.txt', encoding="utf8") as f:
     y1903a = f.read()
with open('r190328.txt', encoding="utf8") as f:
     y1903b = f.read()
with open('r190430.txt', encoding="utf8") as f:
     y1904 = f.read()     
with open('r190606.txt', encoding="utf8") as f:
     y1906a = f.read()
with open('r190617.txt', encoding="utf8") as f:
     y1906b = f.read()
with open('r190618.txt', encoding="utf8") as f:
     y1906c = f.read()
with open('r190627.txt', encoding="utf8") as f:
     y1906d = f.read()
with open('r190712.txt', encoding="utf8") as f:
     y1907a = f.read()
with open('r190716.txt', encoding="utf8") as f:
     y1907b = f.read()
with open('r190827.txt', encoding="utf8") as f:
     y1908 = f.read()
with open('r190924.txt', encoding="utf8") as f:
     y1909 = f.read()
with open('r191008.txt', encoding="utf8") as f:
     y1910a = f.read()
with open('r191014.txt', encoding="utf8") as f:
     y1910b = f.read()
with open('r191211.txt', encoding="utf8") as f:
     y1912a = f.read()
with open('r191218.txt', encoding="utf8") as f:
     y1912b = f.read()

with open('r200109.txt', encoding="utf8") as f:
     y2001 = f.read()
with open('r200304.txt', encoding="utf8") as f:
     y2003a = f.read()
with open('r200306.txt', encoding="utf8") as f:
     y2003b = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2018-04-20','2018-05-14','2018-05-28','2018-06-11','2018-06-27','2018-07-24','2018-09-14','2018-10-25','2018-11-05','2018-11-22',
'2019-02-12','2019-03-22','2019-03-28','2019-04-30','2019-06-06','2019-06-17','2019-06-18','2019-06-27','2019-07-12','2019-07-16','2019-08-27','2019-09-24','2019-10-08','2019-10-14','2019-12-11','2019-12-18',
'2020-01-20','2020-03-04','2020-03-06']

df['text'] = [y1804,y1805a,y1805b,y1806a,y1806b,y1807,y1809,y1810,y1811a,y1811b,    
y1902,y1903a,y1903b,y1904,y1906a,y1906b,y1906c,y1906d,y1907a,y1907b,y1908,y1909,y1910a,y1910b,y1912a,y1912b,
y2001,y2003a,y2003b]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_car3'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()