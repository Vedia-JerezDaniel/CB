### DRAGUI ONE SPEECHES

with open('r130924.txt', encoding="utf8") as f:
     y1309 = f.read()
with open('r131003.txt', encoding="utf8") as f:
     y1310a = f.read()
with open('r131007.txt', encoding="utf8") as f:
     y1310b = f.read()
with open('r131010.txt', encoding="utf8") as f:
     y1310c = f.read()
with open('r131011.txt', encoding="utf8") as f:
     y1310d = f.read()
with open('r131014.txt', encoding="utf8") as f:
     y1310e = f.read()
with open('r131108.txt', encoding="utf8") as f:
     y1311a = f.read()
with open('r131122.txt', encoding="utf8") as f:
     y1311b = f.read()
with open('r131125.txt', encoding="utf8") as f:
     y1311c = f.read()
with open('r131205.txt', encoding="utf8") as f:
     y1312a = f.read()
with open('r131211.txt', encoding="utf8") as f:
     y1312b = f.read()
with open('r131212.txt', encoding="utf8") as f:
     y1312c = f.read()
with open('r131217.txt', encoding="utf8") as f:
     y1312d = f.read()

with open('r140110.txt', encoding="utf8") as f:
     y1401 = f.read()
with open('r140212.txt', encoding="utf8") as f:
     y1402a = f.read()
with open('r140213.txt', encoding="utf8") as f:
     y1402b = f.read()
with open('r140228.txt', encoding="utf8") as f:
     y1402c = f.read()
with open('r140304.txt', encoding="utf8") as f:
     y1403a = f.read()
with open('r140307.txt', encoding="utf8") as f:
     y1403b = f.read()     
with open('r140314.txt', encoding="utf8") as f:
     y1403c = f.read()
with open('r140326.txt', encoding="utf8") as f:
     y1403d = f.read()
with open('r140404.txt', encoding="utf8") as f:
     y1404a = f.read()
with open('r140411.txt', encoding="utf8") as f:
     y1404b = f.read()
with open('r140424.txt', encoding="utf8") as f:
     y1404c = f.read()

with open('r140509.txt', encoding="utf8") as f:
     y1405a = f.read()
with open('r140526.txt', encoding="utf8") as f:
     y1405b = f.read()
with open('r140605.txt', encoding="utf8") as f:
     y1406 = f.read()
with open('r140704.txt', encoding="utf8") as f:
     y1407a = f.read()
with open('r140711.txt', encoding="utf8") as f:
     y1407b = f.read()
with open('r140718.txt', encoding="utf8") as f:
     y1407c = f.read()
with open('r140805.txt', encoding="utf8") as f:
     y1408a = f.read()
with open('r140808.txt', encoding="utf8") as f:
     y1408b = f.read()
with open('r140826.txt', encoding="utf8") as f:
     y1408c = f.read()
with open('r140904.txt', encoding="utf8") as f:
     y1409a = f.read()
with open('r140916.txt', encoding="utf8") as f:
     y1409b= f.read()
with open('r140923.txt', encoding="utf8") as f:
     y1409c = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2013-09-26','2013-10-03','2013-10-07','2013-10-10','2013-10-11','2013-10-14','2013-11-08','2013-11-22','2013-11-25','2013-12-05','2013-12-11','2013-12-12','2013-12-17',
'2014-01-10','2014-02-12','2014-02-13','2014-02-28','2014-03-04','2014-03-07','2014-03-14','2014-03-26','2014-04-04','2014-04-11','2014-04-24','2014-05-09','2014-05-26','2014-06-05','2014-07-04', '2014-07-11','2014-07-18',
'2014-08-05','2014-08-08','2014-08-26','2014-09-04','2014-09-16','2014-09-23']

df.shape

df['text'] = [y1309,y1310a,y1310b,y1310c,y1310d,y1310e,y1311a,y1311b,y1311c,y1312a,y1312b,y1312c,y1312d,
y1401,y1402a,y1402b,y1402c,y1403a,y1403b,y1403c,y1403d,y1404a,y1404b,y1404c,y1405a,y1405b,y1406,y1407a,y1407b,y1407c,y1408a,y1408b,y1408c,y1409a,y1409b,y1409c]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))
df.drop('text', axis=1, inplace=True)
df.rename({'ntex':'text'}, axis=1, inplace=True)

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_dra3'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()
