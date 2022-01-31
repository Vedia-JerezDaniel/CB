### DRAGUI ONE SPEECHES

with open('r121026.txt', encoding="utf8") as f:
     y1210 = f.read()
with open('r121108.txt', encoding="utf8") as f:
     y1211a = f.read()
with open('r121109.txt', encoding="utf8") as f:
     y1211b = f.read()
with open('r121116.txt', encoding="utf8") as f:
     y1211c = f.read()
with open('r121126.txt', encoding="utf8") as f:
     y1211d = f.read()
with open('r121130.txt', encoding="utf8") as f:
     y1211e = f.read()
with open('r121206.txt', encoding="utf8") as f:
     y1212a = f.read()
with open('r121210.txt', encoding="utf8") as f:
     y1212b = f.read()
with open('r121218.txt', encoding="utf8") as f:
     y1212c = f.read()


with open('r130111.txt', encoding="utf8") as f:
     y1301a = f.read()
with open('r130124.txt', encoding="utf8") as f:
     y1301b = f.read()
with open('r130208.txt', encoding="utf8") as f:
     y1302a = f.read()
with open('r130213.txt', encoding="utf8") as f:
     y1302b = f.read()
with open('r130218.txt', encoding="utf8") as f:
     y1302c = f.read()
with open('r130219.txt', encoding="utf8") as f:
     y1302d = f.read()     
with open('r130228.txt', encoding="utf8") as f:
     y1302e = f.read()
with open('r130308.txt', encoding="utf8") as f:
     y1303a = f.read()
with open('r130319.txt', encoding="utf8") as f:
     y1303b = f.read()
with open('r130404.txt', encoding="utf8") as f:
     y1304a = f.read()
with open('r130416.txt', encoding="utf8") as f:
     y1304b = f.read()
with open('r130417.txt', encoding="utf8") as f:
     y1304c = f.read()

with open('r130503.txt', encoding="utf8") as f:
     y1305a = f.read()
with open('r130507.txt', encoding="utf8") as f:
     y1305b = f.read()
with open('r130524.txt', encoding="utf8") as f:
     y1305c = f.read()
with open('r130604.txt', encoding="utf8") as f:
     y1306a = f.read()
with open('r130607.txt', encoding="utf8") as f:
     y1306b = f.read()
with open('r130614.txt', encoding="utf8") as f:
     y1306c = f.read()
with open('r130618.txt', encoding="utf8") as f:
     y1306d = f.read()
with open('r130626.txt', encoding="utf8") as f:
     y1306e = f.read()
with open('r130705.txt', encoding="utf8") as f:
     y1307a = f.read()
with open('r130709.txt', encoding="utf8") as f:
     y1307b = f.read()
with open('r130802.txt', encoding="utf8") as f:
     y1308 = f.read()
with open('r130906.txt', encoding="utf8") as f:
     y1309a = f.read()
with open('r130913.txt', encoding="utf8") as f:
     y1309b = f.read()
with open('r130916.txt', encoding="utf8") as f:
     y1309c = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2012-10-26','2012-11-08','2012-11-09','2012-11-16','2012-11-26','2012-11-30','2012-12-06','2012-12-10','2012-12-18',
'2013-01-15','2013-01-27','2013-02-05','2013-02-13','2013-02-18','2013-02-19','2013-02-28','2013-03-09','2013-03-19','2013-04-05','2013-04-16','2013-04-17','2013-05-03','2013-05-07','2013-05-24','2013-06-04','2013-06-07','2013-06-14','2013-06-18','2013-06-26','2013-07-05', '2013-07-09',
'2013-08-02','2013-09-06','2013-09-13','2013-09-16']

df['text'] = [y1210,y1211a,y1211b,y1211c,y1211d,y1211e,y1212a,y1212b,y1212c,  
y1301a,y1301b,y1302a,y1302b,y1302c,y1302d,y1302e,y1303a,y1303b,y1304a,y1304b,y1304c,y1305a,y1305b,y1305c,y1306a,y1306b,y1306c,y1306d,y1306e,y1307a,y1307b,y1308,y1309a,y1309b,y1309c]

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
db = 'df_dra2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()