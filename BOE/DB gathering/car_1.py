### CARNEY ONE SPEECHES

with open('r130725.txt', encoding="utf8") as f:
     y1307 = f.read()
with open('r130829.txt', encoding="utf8") as f:
     y1308 = f.read()
with open('r131025.txt', encoding="utf8") as f:
     y1310 = f.read()
with open('r131211.txt', encoding="utf8") as f:
     y1312a = f.read()
with open('r131218.txt', encoding="utf8") as f:
     y1312b = f.read()
with open('r140124.txt', encoding="utf8") as f:
     y1401a = f.read()
with open('r140129.txt', encoding="utf8") as f:
     y1401b = f.read()
with open('r140319.txt', encoding="utf8") as f:
     y1403 = f.read()
with open('r140528.txt', encoding="utf8") as f:
     y1405 = f.read()
with open('r140613.txt', encoding="utf8") as f:
     y1406 = f.read()
with open('r140729.txt', encoding="utf8") as f:
     y1407 = f.read()
with open('r140910.txt', encoding="utf8") as f:
     y1409a = f.read()
with open('r140926.txt', encoding="utf8") as f:
     y1409b = f.read()     
with open('r141015.txt', encoding="utf8") as f:
     y1410 = f.read()
with open('r141117.txt', encoding="utf8") as f:
     y1411 = f.read()
with open('r150129.txt', encoding="utf8") as f:
     y1501 = f.read()
with open('r150227.txt', encoding="utf8") as f:
     y1502 = f.read()
with open('r150313.txt', encoding="utf8") as f:
     y1503 = f.read()
with open('r150615.txt', encoding="utf8") as f:
     y1506 = f.read()
with open('r150720.txt', encoding="utf8") as f:
     y1507 = f.read()
with open('r150902.txt', encoding="utf8") as f:
     y1509a = f.read()
with open('r150922.txt', encoding="utf8") as f:
     y1509b = f.read()
with open('r151009.txt', encoding="utf8") as f:
     y1510a = f.read()
with open('r151027.txt', encoding="utf8") as f:
     y1510b = f.read()
with open('r151116.txt', encoding="utf8") as f:
     y1511a = f.read()
with open('r151130.txt', encoding="utf8") as f:
     y1511b = f.read()
with open('r151223.txt', encoding="utf8") as f:
     y1512 = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2013-07-25','2013-08-29','2013-10-25','2013-12-11','2013-12-18','2014-01-24','2014-01-29','2014-03-19','2014-05-28','2014-06-13','2014-07-29','2014-09-10','2014-09-26','2014-10-15','2014-11-17','2015-01-29','2015-02-27','2015-03-13','2015-06-15','2015-07-20','2015-09-02','2015-09-22','2015-10-09','2015-10-27','2015-11-16','2015-11-30','2015-12-23']

df['text'] = [y1307,y1308,y1310,y1312a,y1312b,
y1401a,y1401b,y1403,y1405,y1406,y1407,y1409a, y1409b,y1410,y1411,
y1501,y1502,y1503,y1506,y1507,y1509a,y1509b,y1510a,y1510b,y1511a,y1511b,y1512]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_car1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()