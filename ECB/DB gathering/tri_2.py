
with open('r091106.txt', encoding="utf8") as f:
     y0911a = f.read()
with open('r091120.txt', encoding="utf8") as f:
     y0911b = f.read()
with open('r091123.txt', encoding="utf8") as f:
     y0911c = f.read()
with open('r091125.txt', encoding="utf8") as f:
     y0911d = f.read()
with open('r091126.txt', encoding="utf8") as f:
     y0911e = f.read()
with open('r091202.txt', encoding="utf8") as f:
     y0912a = f.read()
with open('r091208.txt', encoding="utf8") as f:
     y0912b = f.read()
with open('r091211.txt', encoding="utf8") as f:
     y0912c = f.read()
with open('r091217.txt', encoding="utf8") as f:
     y0912d = f.read()
with open('r091218.txt', encoding="utf8") as f:
     y0912e = f.read()

with open('r100120.txt', encoding="utf8") as f:
     y1001a = f.read()
with open('r100126.txt', encoding="utf8") as f:
     y1001b = f.read()
with open('r100205.txt', encoding="utf8") as f:
     y1002a = f.read()
with open('r100211.txt', encoding="utf8") as f:
     y1002b = f.read()     
with open('r100305.txt', encoding="utf8") as f:
     y1003a = f.read()
with open('r100316.txt', encoding="utf8") as f:
     y1003b = f.read()
with open('r100322.txt', encoding="utf8") as f:
     y1003c = f.read()
with open('r100324.txt', encoding="utf8") as f:
     y1003d = f.read()
with open('r100329.txt', encoding="utf8") as f:
     y1003e = f.read()
with open('r100330.txt', encoding="utf8") as f:
     y1003f = f.read()
with open('r100401.txt', encoding="utf8") as f:
     y1004a = f.read()
with open('r100409.txt', encoding="utf8") as f:
     y1004b = f.read()
with open('r100414.txt', encoding="utf8") as f:
     y1004c = f.read()
with open('r100415.txt', encoding="utf8") as f:
     y1004d = f.read()
with open('r100416.txt', encoding="utf8") as f:
     y1004e = f.read()
with open('r100428.txt', encoding="utf8") as f:
     y1004f = f.read()
with open('r100429.txt', encoding="utf8") as f:
     y1004g = f.read()
with open('r100503.txt', encoding="utf8") as f:
     y1005a = f.read()
with open('r100507.txt', encoding="utf8") as f:
     y1005b = f.read()
with open('r100510.txt', encoding="utf8") as f:
     y1005c = f.read()
with open('r100520.txt', encoding="utf8") as f:
     y1005d = f.read()
with open('r100521.txt', encoding="utf8") as f:
     y1005e = f.read()
with open('r100601.txt', encoding="utf8") as f:
     y1006a = f.read()
with open('r100602.txt', encoding="utf8") as f:
     y1006b = f.read()
with open('r100610.txt', encoding="utf8") as f:
     y1006c = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2009-11-06','2009-11-20','2009-11-23','2009-11-25','2009-11-26','2009-12-02',
'2009-12-08','2009-12-11','2009-12-17','2009-12-18',
'2010-01-20','2010-01-26','2010-02-05','2010-02-11','2010-03-05','2010-03-16','2010-03-22','2010-03-24','2010-03-29','2010-03-30','2010-04-01','2010-04-09','2010-04-14','2010-04-15','2010-04-16','2010-04-28','2010-04-29',
'2010-05-03','2010-05-09','2010-05-10','2010-05-20','2010-05-21','2010-06-01','2010-06-02','2010-06-10']
df.shape

df['text'] = [y0911a,y0911b,y0911c,y0911d,y0911e,y0912a,y0912b,y0912c,y0912d,y0912e,
y1001a,y1001b,y1002a,y1002b,y1003a,y1003b,y1003c,y1003d,y1003e,y1003f,y1004a,y1004b,y1004c,y1004d,y1004e,y1004f,y1004g,
y1005a,y1005b,y1005c,y1005d,y1005e,y1006a,y1006b,y1006c]

df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_tri2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()