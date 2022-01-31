with open('r110419.txt', encoding="utf8") as f:
     y1104 = f.read()
with open('r110510.txt', encoding="utf8") as f:
     y1105a = f.read()
with open('r110526.txt', encoding="utf8") as f:
     y1105b = f.read()
with open('r110606.txt', encoding="utf8") as f:
     y1106a = f.read()
with open('r110623.txt', encoding="utf8") as f:
     y1106b = f.read()
with open('r110708.txt', encoding="utf8") as f:
     y1107a = f.read()
with open('r110715.txt', encoding="utf8") as f:
     y1107b = f.read()
with open('r110726.txt', encoding="utf8") as f:
     y1107c = f.read()
with open('r110810.txt', encoding="utf8") as f:
     y1108 = f.read()
with open('r111005.txt', encoding="utf8") as f:
     y1110 = f.read()
with open('r111108.txt', encoding="utf8") as f:
     y1111a = f.read()
with open('r111115.txt', encoding="utf8") as f:
     y1111b = f.read()
with open('r111201.txt', encoding="utf8") as f:
     y1112a = f.read()
with open('r111227.txt', encoding="utf8") as f:
     y1112b = f.read()

with open('r120113.txt', encoding="utf8") as f:
     y1201 = f.read()
with open('r120210.txt', encoding="utf8") as f:
     y1202a = f.read()
with open('r120221.txt', encoding="utf8") as f:
     y1202b = f.read()
with open('r120329.txt', encoding="utf8") as f:
     y1203 = f.read()     
with open('r120420.txt', encoding="utf8") as f:
     y1204a = f.read()
with open('r120423.txt', encoding="utf8") as f:
     y1204b = f.read()
with open('r120531.txt', encoding="utf8") as f:
     y1205 = f.read()
with open('r120608.txt', encoding="utf8") as f:
     y1206a = f.read()
with open('r120614.txt', encoding="utf8") as f:
     y1206b = f.read()
with open('r120802.txt', encoding="utf8") as f:
     y1208 = f.read()
with open('r120907.txt', encoding="utf8") as f:
     y1209 = f.read()
with open('r121009.txt', encoding="utf8") as f:
     y1210a = f.read()
with open('r121010.txt', encoding="utf8") as f:
     y1210b = f.read()
with open('r121015.txt', encoding="utf8") as f:
     y1210c = f.read()
with open('r121113.txt', encoding="utf8") as f:
     y1211a = f.read()
with open('r121127.txt', encoding="utf8") as f:
     y1211b = f.read()
with open('r121203.txt', encoding="utf8") as f:
     y1212 = f.read()
    
with open('r130130.txt', encoding="utf8") as f:
     y1301 = f.read()
with open('r130315.txt', encoding="utf8") as f:
     y1303 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2011-04-24','2011-05-06','2011-05-26','2011-06-03','2011-06-23','2011-07-08','2011-07-15','2011-07-26','2011-08-14','2011-10-15','2011-11-08','2011-11-15','2011-12-04','2011-12-27',
'2012-01-09','2012-02-10','2012-02-21','2012-03-09','2012-04-20','2012-04-26','2012-05-31','2012-06-08','2012-06-14','2012-08-02','2012-09-07','2012-10-09','2012-10-10','2012-10-15','2012-11-08','2012-11-27','2012-12-02',
'2013-01-30','2013-03-15']
df.shape

df['text'] = [y1104,y1105a,y1105b,y1106a,y1106b,y1107a,y1107b,y1107c,y1108,y1110,y1111a,y1111b,y1112a, y1112b,
y1201,y1202a,y1202b,y1203,y1204a,y1204b,y1205,y1206a,y1206b,y1208,y1209,y1210a,y1210b,y1210c,y1211a,y1211b,y1212,
y1301,y1303]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_shi2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()