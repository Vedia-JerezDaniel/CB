
with open('r160927.txt', encoding="utf8") as f:
     y1609a = f.read()
with open('r160928.txt', encoding="utf8") as f:
     y1609b = f.read()
with open('r160929.txt', encoding="utf8") as f:
     y1609c = f.read()
with open('r161003.txt', encoding="utf8") as f:
     y1610a = f.read()
with open('r161012.txt', encoding="utf8") as f:
     y1610b = f.read()
with open('r161021.txt', encoding="utf8") as f:
     y1610c = f.read()
with open('r161026.txt', encoding="utf8") as f:
     y1610d = f.read()
with open('r161128.txt', encoding="utf8") as f:
     y1611 = f.read()
with open('r161201.txt', encoding="utf8") as f:
     y1612a = f.read()
with open('r161202.txt', encoding="utf8") as f:
     y1612b = f.read()
with open('r161206.txt', encoding="utf8") as f:
     y1612c = f.read()
with open('r161212.txt', encoding="utf8") as f:
     y1612d = f.read()

with open('r170119.txt', encoding="utf8") as f:
     y1701a = f.read()
with open('r170125.txt', encoding="utf8") as f:
     y1701b = f.read()
with open('r170131.txt', encoding="utf8") as f:
     y1701c = f.read()
with open('r170203.txt', encoding="utf8") as f:
     y1702a = f.read()
with open('r170209.txt', encoding="utf8") as f:
     y1702b = f.read()
with open('r170310.txt', encoding="utf8") as f:
     y1703a = f.read()
with open('r170314.txt', encoding="utf8") as f:
     y1703b = f.read()     
with open('r170407.txt', encoding="utf8") as f:
     y1704a = f.read()
with open('r170410.txt', encoding="utf8") as f:
     y1704b = f.read()
with open('r170426.txt', encoding="utf8") as f:
     y1704c = f.read()
with open('r170428.txt', encoding="utf8") as f:
     y1704d = f.read()
    
with open('r170505.txt', encoding="utf8") as f:
     y1705a = f.read()
with open('r170510.txt', encoding="utf8") as f:
     y1705b = f.read()
with open('r170522.txt', encoding="utf8") as f:
     y1705c = f.read()
with open('r170607.txt', encoding="utf8") as f:
     y1706a = f.read()
with open('r170608.txt', encoding="utf8") as f:
     y1706b = f.read()
with open('r170609.txt', encoding="utf8") as f:
     y1706c = f.read()
with open('r170314.txt', encoding="utf8") as f:
     y1703b = f.read()     
with open('r170707.txt', encoding="utf8") as f:
     y1707 = f.read()
with open('r170824.txt', encoding="utf8") as f:
     y1708a = f.read()
with open('r170829.txt', encoding="utf8") as f:
     y1708b = f.read()
with open('r170907.txt', encoding="utf8") as f:
     y1709a = f.read()
with open('r170922.txt', encoding="utf8") as f:
     y1709b = f.read()
with open('r170927.txt', encoding="utf8") as f:
     y1709c = f.read()
with open('r171017.txt', encoding="utf8") as f:
     y1710 = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2016-09-27','2016-09-28','2016-09-29','2016-10-03','2016-10-12','2016-10-21','2016-10-26','2016-11-28','2016-12-01','2016-12-02','2016-12-06','2016-12-12',
'2017-01-19','2017-01-25','2017-01-31','2017-02-03','2017-02-09','2017-03-10','2017-03-14','2017-04-07','2017-04-10','2017-04-26','2017-04-28','2017-05-05','2017-05-10','2017-05-22',
'2017-06-07','2017-06-08','2017-06-09','2017-07-07','2017-08-23','2017-08-29','2017-09-07','2017-09-22','2017-09-27','2017-10-17']

df.shape

df['text'] = [y1609a,y1609b,y1609c,y1610a,y1610b,y1610c,y1610d,y1611,y1612a,y1612b,y1612c,y1612d,
y1701a,y1701b,y1701c,y1702a,y1702b,y1703a,y1703b,y1704a,y1704b,y1704c,y1704d,
y1705a,y1705b,y1705c,y1706a,y1706b,y1706c,y1707,y1708a,y1708b,y1709a,y1709b,y1709c,y1710]  

df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_dra5'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()