with open('r140212.txt', encoding="utf8") as f:
     y1402 = f.read()
with open('r140307.txt', encoding="utf8") as f:
     y1403a = f.read()
with open('r140326.txt', encoding="utf8") as f:
     y1403b = f.read()
with open('r140401.txt', encoding="utf8") as f:
     y1404a = f.read()
with open('r140417.txt', encoding="utf8") as f:
     y1404b = f.read()
with open('r140502.txt', encoding="utf8") as f:
     y1405a = f.read()
with open('r140508.txt', encoding="utf8") as f:
     y1405b = f.read()
with open('r140516.txt', encoding="utf8") as f:
     y1405c = f.read()
with open('r140522.txt', encoding="utf8") as f:
     y1405d = f.read()
with open('r140703.txt', encoding="utf8") as f:
     y1407 = f.read()
with open('r140822.txt', encoding="utf8") as f:
     y1408 = f.read()
with open('r140918.txt', encoding="utf8") as f:
     y1409 = f.read()
with open('r141020.txt', encoding="utf8") as f:
     y1410a = f.read()
with open('r141031.txt', encoding="utf8") as f:
     y1410b = f.read()
with open('r141110.txt', encoding="utf8") as f:
     y1411 = f.read()

with open('r150225.txt', encoding="utf8") as f:
     y1502 = f.read()
with open('r150304.txt', encoding="utf8") as f:
     y1503 = f.read()
with open('r150401.txt', encoding="utf8") as f:
     y1504a = f.read()
with open('r150408.txt', encoding="utf8") as f:
     y1504b = f.read()
with open('r150507.txt', encoding="utf8") as f:
     y1505a = f.read()
with open('r150528.txt', encoding="utf8") as f:
     y1505b = f.read()
with open('r150714.txt', encoding="utf8") as f:
     y1507a = f.read()     
with open('r150716.txt', encoding="utf8") as f:
     y1507b = f.read()
with open('r150928.txt', encoding="utf8") as f:
     y1509 = f.read()
with open('r151001.txt', encoding="utf8") as f:
     y1510a = f.read()
with open('r151021.txt', encoding="utf8") as f:
     y1510b = f.read()
with open('r151105.txt', encoding="utf8") as f:
     y1511a = f.read()
with open('r151113.txt', encoding="utf8") as f:
     y1511b = f.read()
with open('r151204.txt', encoding="utf8") as f:
     y1512a = f.read()
with open('r151207.txt', encoding="utf8") as f:
     y1512b = f.read()
with open('r160211.txt', encoding="utf8") as f:
     y1602 = f.read()     
with open('r160401.txt', encoding="utf8") as f:
     y1604 = f.read()
with open('r160607.txt', encoding="utf8") as f:
     y1606a = f.read()
with open('r160623.txt', encoding="utf8") as f:
     y1606b = f.read()
with open('r160829.txt', encoding="utf8") as f:
     y1608 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2014-02-12','2014-03-07','2014-03-26','2014-04-01','2014-04-17','2014-05-02','2014-05-08','2014-05-16','2014-05-22','2014-07-03','2014-08-17','2014-09-17','2014-10-20','2014-10-31','2014-11-10',
'2015-02-12','2015-03-05','2015-04-01','2015-04-08','2015-05-07','2015-05-28','2015-07-13','2015-07-16','2015-09-24','2015-10-01','2015-10-21','2015-11-06','2015-11-13','2015-12-04','2015-12-07',
'2016-02-11','2016-04-02','2016-06-05','2016-06-23','2016-08-29']
df.shape

df['text'] = [y1402,y1403a,y1403b,y1404a,y1404b,y1405a,y1405b,y1405c,y1405d,y1407,y1408,y1409,y1410a,y1410b,y1411,
y1502,y1503,y1504a,y1504b,y1505a,y1505b,y1507a,y1507b,y1509,y1510a,y1510b,y1511a,y1511b,y1512a,y1512b,
y1602,y1604,y1606a,y1606b,y1608]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_yel1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()

