with open('r171019.txt', encoding="utf8") as f:
     y1710a = f.read()
with open('r171026.txt', encoding="utf8") as f:
     y1710b = f.read()
with open('r171107.txt', encoding="utf8") as f:
     y1711a = f.read()
with open('r171121.txt', encoding="utf8") as f:
     y1711b = f.read()
with open('r171122.txt', encoding="utf8") as f:
     y1711c = f.read()
with open('r171222.txt', encoding="utf8") as f:
     y1712 = f.read()

with open('r180125.txt', encoding="utf8") as f:
     y1801 = f.read()
with open('r180206.txt', encoding="utf8") as f:
     y1802 = f.read()
with open('r180302.txt', encoding="utf8") as f:
     y1803a = f.read()
with open('r180314.txt', encoding="utf8") as f:
     y1803b = f.read()
with open('r180319.txt', encoding="utf8") as f:
     y1803c = f.read()
with open('r180423.txt', encoding="utf8") as f:
     y1804 = f.read()
with open('r180503.txt', encoding="utf8") as f:
     y1805a = f.read()
with open('r180516.txt', encoding="utf8") as f:
     y1805b = f.read()
with open('r180719.txt', encoding="utf8") as f:
     y1807a = f.read()
with open('r180719.txt', encoding="utf8") as f:
     y1807b = f.read()
with open('r180726.txt', encoding="utf8") as f:
     y1807c = f.read()
with open('r180913.txt', encoding="utf8") as f:
     y1809a = f.read()
with open('r180918.txt', encoding="utf8") as f:
     y1809b = f.read()
with open('r180926.txt', encoding="utf8") as f:
     y1809c = f.read()     
with open('r181012.txt', encoding="utf8") as f:
     y1810a = f.read()
with open('r181029.txt', encoding="utf8") as f:
     y1810b = f.read()
with open('r181109.txt', encoding="utf8") as f:
     y1811a = f.read()
with open('r181116.txt', encoding="utf8") as f:
     y1811b = f.read()
with open('r181127.txt', encoding="utf8") as f:
     y1811c = f.read()
with open('r181213.txt', encoding="utf8") as f:
     y1812a = f.read()
with open('r181218.txt', encoding="utf8") as f:
     y1812b = f.read()

with open('r190115.txt', encoding="utf8") as f:
     y1901a = f.read()
with open('r190116.txt', encoding="utf8") as f:
     y1901b = f.read()
with open('r190124.txt', encoding="utf8") as f:
     y1901c = f.read()
with open('r190128.txt', encoding="utf8") as f:
     y1901d = f.read()
with open('r190225.txt', encoding="utf8") as f:
     y1902 = f.read()
with open('r190312.txt', encoding="utf8") as f:
     y1903a = f.read()
with open('r190327.txt', encoding="utf8") as f:
     y1903b = f.read()     
with open('r190410.txt', encoding="utf8") as f:
     y1904a = f.read()
with open('r190429.txt', encoding="utf8") as f:
     y1904b = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2017-10-19','2017-10-28','2017-11-07','2017-11-21','2017-11-22','2017-12-21',
'2018-01-25','2018-02-06','2018-03-02','2018-03-14','2018-03-19','2018-04-23','2018-05-03','2018-05-10','2018-07-17','2018-07-19','2018-07-26','2018-09-13','2018-09-18','2018-09-26','2018-10-12','2018-10-29','2018-11-09','2018-11-17','2018-11-23','2018-12-13','2018-12-18',
'2019-01-15','2019-01-16','2019-01-24','2019-01-28','2019-02-27','2019-03-12','2019-03-27','2019-04-12','2019-04-29']
df.shape

df['text'] = [y1710a,y1710b,y1711a,y1711b,y1711c,y1712,
y1801,y1802,y1803a,y1803b,y1803c,y1804,y1805a,y1805b,y1807a,y1807b,y1807c,
y1809a,y1809b,y1809c,y1810a,y1810b,y1811a,y1811b,y1811c,y1812a,y1812b,
y1901a,y1901b,y1901c,y1901d,y1902,y1903a,y1903b,y1904a,y1904b]  
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_dra6'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()