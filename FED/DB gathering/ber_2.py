with open('r100408.txt', encoding="utf8") as f:
     y1004a = f.read()
with open('r100412.txt', encoding="utf8") as f:
     y1004b = f.read()
with open('r100415.txt', encoding="utf8") as f:
     y1004c = f.read()
with open('r100419.txt', encoding="utf8") as f:
     y1004d = f.read()     
with open('r100422.txt', encoding="utf8") as f:
     y1004e = f.read()
with open('r100423.txt', encoding="utf8") as f:
     y1004f = f.read()
with open('r100429.txt', encoding="utf8") as f:
     y1004g = f.read()
with open('r100507.txt', encoding="utf8") as f:
     y1005a = f.read()
with open('r100511.txt', encoding="utf8") as f:
     y1005b = f.read()
with open('r100527.txt', encoding="utf8") as f:
     y1005c = f.read()
with open('r100601.txt', encoding="utf8") as f:
     y1006a = f.read()
with open('r100608.txt', encoding="utf8") as f:
     y1006b = f.read()
with open('r100610.txt', encoding="utf8") as f:
     y1006c = f.read()
with open('r100614.txt', encoding="utf8") as f:
     y1006d = f.read()
with open('r100618.txt', encoding="utf8") as f:
     y1006e = f.read()
with open('r100726.txt', encoding="utf8") as f:
     y1007 = f.read()
with open('r100804.txt', encoding="utf8") as f:
     y1008a = f.read()
with open('r100830.txt', encoding="utf8") as f:
     y1008b = f.read()

with open('r100929.txt', encoding="utf8") as f:
     y1009a = f.read()
with open('r100930.txt', encoding="utf8") as f:
     y1009b = f.read()
with open('r101007.txt', encoding="utf8") as f:
     y1010a = f.read()
with open('r101020.txt', encoding="utf8") as f:
     y1010b = f.read()
with open('r101022.txt', encoding="utf8") as f:
     y1010c = f.read()
with open('r101029.txt', encoding="utf8") as f:
     y1010d = f.read()
with open('r101125.txt', encoding="utf8") as f:
     y1011a = f.read()
with open('r101126.txt', encoding="utf8") as f:
     y1011b = f.read()

with open('r110107.txt', encoding="utf8") as f:
     y1101 = f.read()
with open('r110204.txt', encoding="utf8") as f:
     y1102a = f.read()
with open('r110209.txt', encoding="utf8") as f:
     y1102b = f.read()
with open('r110217.txt', encoding="utf8") as f:
     y1102c = f.read()
with open('r110221.txt', encoding="utf8") as f:
     y1102d = f.read()
with open('r110302.txt', encoding="utf8") as f:
     y1103a = f.read()
with open('r110303.txt', encoding="utf8") as f:
     y1103b = f.read()
with open('r110324.txt', encoding="utf8") as f:
     y1103c = f.read()
with open('r110405.txt', encoding="utf8") as f:
     y1104 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2010-04-08','2010-04-12','2010-04-15','2010-04-19','2010-04-22','2010-04-23','2010-04-29','2010-05-07','2010-05-11','2010-05-25','2010-06-01','2010-06-08','2010-06-10','2010-06-14','2010-06-18','2010-06-26',
'2010-08-04','2010-08-30','2010-09-29','2010-09-30','2010-10-07','2010-10-20','2010-10-22','2010-10-29',
'2010-11-25','2010-11-26',
'2011-01-07','2011-02-04','2011-02-09','2011-02-17','2011-02-21','2011-03-02','2011-03-03','2011-03-24','2011-04-05']
df.shape

df['text'] = [y1004a,y1004b,y1004c,y1004d,y1004e,y1004f,y1004g,y1005a,y1005b,y1005c,y1006a,y1006b,y1006c,y1006d,y1006e,y1007,y1008a,y1008b,y1009a,y1009b,y1010a,y1010b,y1010c,y1010d,y1011a,y1011b,
y1101,y1102a,y1102b,y1102c,y1102d,y1103a,y1103b,y1103c,y1104]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_ber2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()