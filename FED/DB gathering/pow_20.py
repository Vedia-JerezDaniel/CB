with open('r200211.txt', encoding="utf8") as f:
     y2002 = f.read()
with open('r200409.txt', encoding="utf8") as f:
     y2004 = f.read()
with open('r200513.txt', encoding="utf8") as f:
     y2005 = f.read()
with open('r200519.txt', encoding="utf8") as f:
     y2005a = f.read()
with open('r200522.txt', encoding="utf8") as f:
     y2005b = f.read()     
with open('r200616.txt', encoding="utf8") as f:
     y2006 = f.read()
with open('r200716.txt', encoding="utf8") as f:
     y2007 = f.read()
with open('r200716b.txt', encoding="utf8") as f:
     y2007a = f.read()
with open('r200827.txt', encoding="utf8") as f:
     y2008 = f.read()
with open('r200922.txt', encoding="utf8") as f:
     y2009 = f.read()
with open('r201007.txt', encoding="utf8") as f:
     y2010 = f.read()
with open('r201201.txt', encoding="utf8") as f:
     y2012 = f.read()
with open('r210211.txt', encoding="utf8") as f:
     y2102 = f.read()
with open('r210223.txt', encoding="utf8") as f:
     y2102a = f.read()
with open('r210319.txt', encoding="utf8") as f:
     y2103 = f.read()
with open('r210323.txt', encoding="utf8") as f:
     y2103a = f.read()
with open('r210504.txt', encoding="utf8") as f:
     y2105 = f.read()
with open('r210622.txt', encoding="utf8") as f:
     y2106 = f.read()
with open('r210714.txt', encoding="utf8") as f:
     y2107 = f.read()
with open('r210820.txt', encoding="utf8") as f:
     y2108 = f.read()
with open('r210902.txt', encoding="utf8") as f:
     y2109 = f.read()
with open('r211012c.txt', encoding="utf8") as f:
     y2110 = f.read()
with open('r211128.txt', encoding="utf8") as f:
     y2111 = f.read()
with open('r211128d.txt', encoding="utf8") as f:
     y2111a = f.read()
     
import pandas as pd
df = pd.DataFrame()

df['date'] = ['2020-02-11','2020-04-09','2020-05-13','2020-05-19','2020-05-22','2020-06-16','2020-07-16','2020-07-17','2020-08-27','2020-09-22','2020-10-07','2020-12-01','2021-02-11','2021-02-23','2021-03-19','2021-03-23','2021-05-04','2021-06-22','2021-07-14','2021-08-18','2021-09-02','2021-10-11','2021-11-20','2021-11-29']
df.shape

df['text'] = [y2002,y2004,y2005,y2005a,y2005b,y2006,y2007,y2007a,y2008,y2009,y2010,y2012,
y2102,y2102a,y2103,y2103a,y2105,y2106,y2107,y2108,y2109,y2110,y2111,y2111a]  
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_pow20'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()