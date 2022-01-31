with open('130328.txt', encoding="utf8") as f:
    y1303 = f.read()
with open('130412.txt', encoding="utf8") as f:
    y1304 = f.read()
with open('130524.txt', encoding="utf8") as f:
    y1305a = f.read()
with open('130527.txt', encoding="utf8") as f:
    y1305b = f.read()
with open('130529.txt', encoding="utf8") as f:
    y1305c = f.read()
with open('130702.txt', encoding="utf8") as f:
    y1307 = f.read()
with open('130802.txt', encoding="utf8") as f:
    y1308a = f.read()
with open('130826.txt', encoding="utf8") as f:
    y1308b = f.read()
with open('130920.txt', encoding="utf8") as f:
    y1309 = f.read()
with open('131016.txt', encoding="utf8") as f:
    y1310 = f.read()
with open('131105.txt', encoding="utf8") as f:
    y1311a = f.read()
with open('131125.txt', encoding="utf8") as f:
    y1311b = f.read()
with open('131203.txt', encoding="utf8") as f:
    y1312a = f.read()
with open('131209.txt', encoding="utf8") as f:
    y1312b = f.read()
with open('131227.txt', encoding="utf8") as f:
    y1312c = f.read()

with open('140321.txt', encoding="utf8") as f:
     y1403a = f.read()
with open('140324.txt', encoding="utf8") as f:
     y1403b = f.read()
with open('140516.txt', encoding="utf8") as f:
     y1405 = f.read()
with open('140610.txt', encoding="utf8") as f:
     y1406a = f.read()
with open('140624.txt', encoding="utf8") as f:
     y1406b = f.read()
with open('140725.txt', encoding="utf8") as f:
     y1407 = f.read()
with open('140805.txt', encoding="utf8") as f:
     y1408a = f.read()
with open('140825.txt', encoding="utf8") as f:
     y1408b = f.read()
with open('140917.txt', encoding="utf8") as f:
     y1409a = f.read()
with open('140929.txt', encoding="utf8") as f:
     y1409b = f.read()
with open('141010.txt', encoding="utf8") as f:
     y1410 = f.read()
with open('141127.txt', encoding="utf8") as f:
     y1411 = f.read()
with open('141202.txt', encoding="utf8") as f:
     y1412 = f.read()

with open('150109.txt', encoding="utf8") as f:
     y1501 = f.read()
with open('150303.txt', encoding="utf8") as f:
     y1503a = f.read()
with open('150320.txt', encoding="utf8") as f:
     y1503b = f.read()
with open('150518.txt', encoding="utf8") as f:
     y1505a = f.read()
with open('150526.txt', encoding="utf8") as f:
     y1505b = f.read()
with open('150605.txt', encoding="utf8") as f:
     y1506 = f.read()   
with open('150702.txt', encoding="utf8") as f:
     y1507 = f.read()   


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2013-03-26','2013-04-03','2013-05-24','2013-05-27','2013-05-29','2013-07-18','2013-08-02','2013-08-27','2013-09-20','2013-10-26','2013-11-05','2013-11-25','2013-12-03','2013-12-09','2013-12-27',
'2014-03-21','2014-03-24','2014-05-22','2014-06-10','2014-06-24','2014-07-25','2014-08-13','2014-08-25','2014-09-15','2014-09-29','2014-10-10','2014-11-29','2014-12-02',
'2015-01-09','2015-03-02','2015-03-20','2015-05-17','2015-05-26','2015-06-08','2015-07-02']
df.shape

df['text'] = [y1303,y1304,y1305a,y1305b,y1305c,y1307,y1308a,y1308b,y1309,y1310,y1311a,y1311b,y1312a,y1312b,y1312c,
y1403a,y1403b,y1405,y1406a,y1406b,y1407,y1408a,y1408b,y1409a,y1409b,y1410,y1411,y1412,
y1501,y1503a,y1503b,y1505a,y1505b,y1506,y1507]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_kur1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()