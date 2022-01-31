with open('r121015.txt', encoding="utf8") as f:
     y1210 = f.read()
with open('r121116.txt', encoding="utf8") as f:
     y1211a = f.read()
with open('r121121.txt', encoding="utf8") as f:
     y1211b = f.read()
with open('r130227.txt', encoding="utf8") as f:
     y1302 = f.read()
with open('r130306.txt', encoding="utf8") as f:
     y1303a = f.read()
with open('r130326.txt', encoding="utf8") as f:
     y1303b = f.read()
with open('r130405.txt', encoding="utf8") as f:
     y1304a = f.read()
with open('r130409.txt', encoding="utf8") as f:
     y1304b = f.read()
with open('r130415.txt', encoding="utf8") as f:
     y1304c = f.read()     
with open('r130514.txt', encoding="utf8") as f:
     y1305a = f.read()
with open('r130523.txt', encoding="utf8") as f:
     y1305b = f.read()
with open('r130604.txt', encoding="utf8") as f:
     y1306 = f.read()
with open('r130712.txt', encoding="utf8") as f:
     y1307a = f.read()
with open('r130717.txt', encoding="utf8") as f:
     y1307b = f.read()

with open('r131004.txt', encoding="utf8") as f:
     y1310 = f.read()
with open('r131107.txt', encoding="utf8") as f:
     y1311a = f.read()
with open('r131111.txt', encoding="utf8") as f:
     y1311b = f.read()
with open('r131114.txt', encoding="utf8") as f:
     y1311c = f.read()
with open('r131115.txt', encoding="utf8") as f:
     y1311d = f.read()
with open('r131120.txt', encoding="utf8") as f:
     y1311e = f.read()
with open('r131217.txt', encoding="utf8") as f:
     y1312a = f.read()
with open('r131231.txt', encoding="utf8") as f:
     y1312b = f.read()
with open('r140106.txt', encoding="utf8") as f:
     y1401 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2012-10-15','2012-11-16','2012-11-21',
'2013-02-27','2013-03-06','2013-03-26','2013-04-05','2013-04-09','2013-04-15','2013-05-14','2013-05-23','2013-06-04','2013-07-12','2013-07-17','2013-10-05','2013-11-07','2013-11-11','2013-11-14','2013-11-15','2013-11-20',
'2013-12-17','2013-12-31','2014-01-06']
df.shape

df['text'] = [y1210,y1211a,y1211b,y1302,y1303a,y1303b,y1304a,y1304b,y1304c,y1305a,y1305b,y1306,y1307a,y1307b,y1310,y1311a,y1311b,y1311c,y1311d,y1311e,y1312a,y1312b,y1401]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_ber4'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()