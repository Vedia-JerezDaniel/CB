with open('r090216.txt', encoding="utf8") as f:
     y0902a = f.read()
with open('r090220.txt', encoding="utf8") as f:
     y0902b = f.read()
with open('r090226.txt', encoding="utf8") as f:
     y0902c = f.read()
with open('r090304.txt', encoding="utf8") as f:
     y0903a = f.read()
with open('r090313.txt', encoding="utf8") as f:
     y0903b = f.read()
with open('r090324.txt', encoding="utf8") as f:
     y0903c = f.read()
with open('r090325.txt', encoding="utf8") as f:
     y0903d = f.read()
with open('r090408.txt', encoding="utf8") as f:
     y0904a = f.read()
with open('r090415.txt', encoding="utf8") as f:
     y0904b = f.read()
with open('r090421.txt', encoding="utf8") as f:
     y0904c = f.read()
with open('r090506.txt', encoding="utf8") as f:
     y0905a = f.read()
with open('r090508.txt', encoding="utf8") as f:
     y0905b = f.read()
with open('r090512.txt', encoding="utf8") as f:
     y0905c = f.read()
with open('r090527.txt', encoding="utf8") as f:
     y0905d = f.read()
 
with open('r090609.txt', encoding="utf8") as f:
     y0906a = f.read()
with open('r090619.txt', encoding="utf8") as f:
     y0906b = f.read()
with open('r090701.txt', encoding="utf8") as f:
     y0907a = f.read()
with open('r090727.txt', encoding="utf8") as f:
     y0907b = f.read()
with open('r090827.txt', encoding="utf8") as f:
     y0908 = f.read()
with open('r090930.txt', encoding="utf8") as f:
     y0909 = f.read()
with open('r091006.txt', encoding="utf8") as f:
     y0910a = f.read()
with open('r091013.txt', encoding="utf8") as f:
     y0910b = f.read()
with open('r091021.txt', encoding="utf8") as f:
     y0910c = f.read()
with open('r091027.txt', encoding="utf8") as f:
     y0910d = f.read()
with open('r091119.txt', encoding="utf8") as f:
     y0911 = f.read()
with open('r091210.txt', encoding="utf8") as f:
     y0912a = f.read()
with open('r091214.txt', encoding="utf8") as f:
     y0912b = f.read()

with open('r100113.txt', encoding="utf8") as f:
     y1001 = f.read()
with open('r100204.txt', encoding="utf8") as f:
     y1002a = f.read()
with open('r100212.txt', encoding="utf8") as f:
     y1002b = f.read()
with open('r100225.txt', encoding="utf8") as f:
     y1002c = f.read()
with open('r100318.txt', encoding="utf8") as f:
     y1003a = f.read()
with open('r100324.txt', encoding="utf8") as f:
     y1003b= f.read()
with open('r100329.txt', encoding="utf8") as f:
     y1003c = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2009-02-16','2009-02-20','2009-02-26','2009-03-04','2009-03-13','2009-03-24','2009-03-25','2009-04-08','2009-04-15','2009-04-21','2009-05-06','2009-05-08','2009-05-12','2009-05-27','2009-06-09','2009-06-19','2009-07-01','2009-07-27','2009-08-27','2009-09-30','2009-10-06','2009-10-13','2009-10-21','2009-10-27',
'2009-11-19','2009-12-10','2009-12-14',
'2010-01-08','2010-02-04','2010-02-12','2010-02-25','2010-03-18','2010-03-24','2010-03-29']
df.shape

df['text'] = [y0902a,y0902b,y0902c,y0903a,y0903b,y0903c,y0903d,y0904a,y0904b,y0904c,y0905a,y0905b,y0905c,y0905d,y0906a,y0906b,y0907a,y0907b,y0908,y0909,y0910a,y0910b,y0910c,y0910d,y0911,y0912a,y0912b,
y1001,y1002a,y1002b,y1002c,y1003a,y1003b,y1003c]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_ber1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()

