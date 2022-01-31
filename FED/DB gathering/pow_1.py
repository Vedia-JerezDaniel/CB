with open('r180228.txt', encoding="utf8") as f:
     y1802 = f.read()
with open('r180307.txt', encoding="utf8") as f:
     y1803 = f.read()
with open('r180508.txt', encoding="utf8") as f:
     y1805 = f.read()
with open('r180723.txt', encoding="utf8") as f:
     y1807 = f.read()
with open('r180827.txt', encoding="utf8") as f:
     y1808 = f.read()
with open('r181001.txt', encoding="utf8") as f:
     y1810a = f.read()
with open('r181003.txt', encoding="utf8") as f:
     y1810b = f.read()
with open('r181129.txt', encoding="utf8") as f:
     y1811 = f.read()
with open('r181206.txt', encoding="utf8") as f:
     y1812a = f.read()
with open('r181207.txt', encoding="utf8") as f:
     y1812b = f.read()
with open('r190207.txt', encoding="utf8") as f:
     y1902a = f.read()
with open('r190213.txt', encoding="utf8") as f:
     y1902b = f.read()
with open('r190226.txt', encoding="utf8") as f:
     y1902c = f.read()
with open('r190301.txt', encoding="utf8") as f:
     y1903a = f.read()
with open('r190315.txt', encoding="utf8") as f:
     y1903b = f.read()     
with open('r190513.txt', encoding="utf8") as f:
     y1905a = f.read()
with open('r190521.txt', encoding="utf8") as f:
     y1905b = f.read()
with open('r190606.txt', encoding="utf8") as f:
     y1906a = f.read()
with open('r190627.txt', encoding="utf8") as f:
     y1906b = f.read()
with open('r190711.txt', encoding="utf8") as f:
     y1907a = f.read()
with open('r190718.txt', encoding="utf8") as f:
     y1907b = f.read()
with open('r190823.txt', encoding="utf8") as f:
     y1908 = f.read()
with open('r191007.txt', encoding="utf8") as f:
     y1910a = f.read()
with open('r191008.txt', encoding="utf8") as f:
     y1910b = f.read()
with open('r191009.txt', encoding="utf8") as f:
     y1910c = f.read()
with open('r191113.txt', encoding="utf8") as f:
     y1911a = f.read()
with open('r191126.txt', encoding="utf8") as f:
     y1911b = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2018-02-25','2018-03-06','2018-05-02','2018-07-14','2018-08-19','2018-10-01','2018-10-03','2018-11-10','2018-12-06','2018-12-07',
'2019-02-07','2019-02-13','2019-02-26','2019-03-01','2019-03-15','2019-05-13','2019-05-21','2019-06-06','2019-06-27','2019-07-11','2019-07-18','2019-08-29','2019-10-07','2019-10-08','2019-10-09','2019-11-18','2019-11-29']
df.shape

df['text'] = [y1802,y1803,y1805,y1807,y1808,y1810a,y1810b,y1811,y1812a,y1812b,
y1902a,y1902b,y1902c,y1903a,y1903b,y1905a,y1905b,y1906a,y1906b,y1907a,y1907b,y1908,
y1910a,y1910b,y1910c,y1911a,y1911b]  
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_pow1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()