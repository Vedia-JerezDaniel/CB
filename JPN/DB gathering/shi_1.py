with open('r090303.txt', encoding="utf8") as f:
     y0903a = f.read()
with open('r090327.txt', encoding="utf8") as f:
     y0903b = f.read()
with open('r090414.txt', encoding="utf8") as f:
     y0904a = f.read()
with open('r090427.txt', encoding="utf8") as f:
     y0904b = f.read()
with open('r090520.txt', encoding="utf8") as f:
     y0905a = f.read()
with open('r090529.txt', encoding="utf8") as f:
     y0905b = f.read()
with open('r090602.txt', encoding="utf8") as f:
     y0906a = f.read()
with open('r090612.txt', encoding="utf8") as f:
     y0906b = f.read()
with open('r090703.txt', encoding="utf8") as f:
     y0907 = f.read()
with open('r090819.txt', encoding="utf8") as f:
     y0908a = f.read()
with open('r090827.txt', encoding="utf8") as f:
     y0908b = f.read()
with open('r090902.txt', encoding="utf8") as f:
     y0909 = f.read()
with open('r091110.txt', encoding="utf8") as f:
     y0911a = f.read()
with open('r091118.txt', encoding="utf8") as f:
     y0911b = f.read()
with open('r091127.txt', encoding="utf8") as f:
     y0911c = f.read()
with open('r091203.txt', encoding="utf8") as f:
     y0912a = f.read()
with open('r091204.txt', encoding="utf8") as f:
     y0912b = f.read()
with open('r091217.txt', encoding="utf8") as f:
     y0912c = f.read()
with open('r091223.txt', encoding="utf8") as f:
     y0912d = f.read()

with open('r100120.txt', encoding="utf8") as f:
     y1001 = f.read()
with open('r100203.txt', encoding="utf8") as f:
     y1002 = f.read()
with open('r100414.txt', encoding="utf8") as f:
     y1004a = f.read()
with open('r100422.txt', encoding="utf8") as f:
     y1004b = f.read()     
with open('r100427.txt', encoding="utf8") as f:
     y1004c = f.read()
with open('r100527.txt', encoding="utf8") as f:
     y1005 = f.read()
with open('r100601.txt', encoding="utf8") as f:
     y1006 = f.read()
with open('r100920.txt', encoding="utf8") as f:
     y1009 = f.read()
with open('r101014.txt', encoding="utf8") as f:
     y1010a = f.read()
with open('r101019.txt', encoding="utf8") as f:
     y1010b = f.read()
with open('r101108.txt', encoding="utf8") as f:
     y1011a = f.read()
with open('r101129.txt', encoding="utf8") as f:
     y1011b = f.read()
with open('r101202.txt', encoding="utf8") as f:
     y1012 = f.read()

with open('r110207.txt', encoding="utf8") as f:
     y1102a = f.read()
with open('r110222.txt', encoding="utf8") as f:
     y1102b = f.read()
with open('r110309.txt', encoding="utf8") as f:
     y1103 = f.read()
with open('r110411.txt', encoding="utf8") as f:
     y1104 = f.read()   


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2009-03-06','2009-03-27','2009-04-14','2009-04-27','2009-05-20','2009-15-29','2009-06-02','2009-06-12','2009-07-03','2009-08-19','2009-08-27','2009-09-06','2009-11-10','2009-11-18','2009-11-27','2009-12-03','2009-12-04','2009-12-17','2009-12-23',
'2010-01-20','2010-02-03','2010-04-14','2010-04-22','2010-04-27','2010-05-27','2010-06-01','2010-09-22','2010-10-14','2010-10-19','2010-11-08','2010-11-29','2010-12-09',
'2011-02-07','2011-02-22','2010-03-09','2010-04-11']
df.shape

df['text'] = [y0903a,y0903b,y0904a,y0904b,y0905a,y0905b,y0906a,y0906b,y0907,y0908a,y0908b,y0909,y0911a,y0911b,y0911c,y0912a,y0912b,y0912c,y0912d,
y1001,y1002,y1004a,y1004b,y1004c,y1005,y1006,y1009,y1010a,y1010b,y1011a,y1011b,y1012,
y1102a,y1102b,y1103,y1104]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_shi1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()