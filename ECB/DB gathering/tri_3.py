with open('r100614.txt', encoding="utf8") as f:
     y1006a = f.read()
with open('r100615.txt', encoding="utf8") as f:
     y1006b = f.read()
with open('r100624.txt', encoding="utf8") as f:
     y1006c = f.read()
with open('r100716.txt', encoding="utf8") as f:
     y1007a = f.read()
with open('r100722.txt', encoding="utf8") as f:
     y1007b = f.read()
with open('r100811.txt', encoding="utf8") as f:
     y1008 = f.read()
with open('r100901.txt', encoding="utf8") as f:
     y1009a = f.read()
with open('r100908.txt', encoding="utf8") as f:
     y1009b = f.read()
with open('r100921.txt', encoding="utf8") as f:
     y1009c = f.read()
with open('r100922.txt', encoding="utf8") as f:
     y1009d = f.read()

with open('r101001.txt', encoding="utf8") as f:
     y1010a = f.read()
with open('r101013.txt', encoding="utf8") as f:
     y1010b = f.read()
with open('r101015.txt', encoding="utf8") as f:
     y1010c = f.read()
with open('r101018.txt', encoding="utf8") as f:
     y1010d = f.read()     
with open('r101020.txt', encoding="utf8") as f:
     y1010e = f.read()
with open('r101021.txt', encoding="utf8") as f:
     y1010f = f.read()
with open('r101022.txt', encoding="utf8") as f:
     y1010g = f.read()
with open('r101108.txt', encoding="utf8") as f:
     y1011a = f.read()
with open('r101117.txt', encoding="utf8") as f:
     y1011b = f.read()
with open('r101124.txt', encoding="utf8") as f:
     y1011c = f.read()
with open('r101126.txt', encoding="utf8") as f:
     y1011d = f.read()
with open('r101129.txt', encoding="utf8") as f:
     y1011e = f.read()
with open('r101206.txt', encoding="utf8") as f:
     y1012a = f.read()
with open('r101207.txt', encoding="utf8") as f:
     y1012b = f.read()
with open('r101214.txt', encoding="utf8") as f:
     y1012c = f.read()
with open('r101217.txt', encoding="utf8") as f:
     y1012d = f.read()

with open('r110110.txt', encoding="utf8") as f:
     y1101a = f.read()
with open('r110113.txt', encoding="utf8") as f:
     y1101b = f.read()
with open('r110202.txt', encoding="utf8") as f:
     y1102a = f.read()
with open('r110204.txt', encoding="utf8") as f:
     y1102b = f.read()
with open('r110214.txt', encoding="utf8") as f:
     y1102c = f.read()
with open('r110221.txt', encoding="utf8") as f:
     y1102d = f.read()
with open('r110224.txt', encoding="utf8") as f:
     y1102e = f.read()
with open('r110304.txt', encoding="utf8") as f:
     y1103a = f.read()
with open('r110322.txt', encoding="utf8") as f:
     y1103b = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2010-06-14','2010-16-15','2010-06-23','2010-07-17','2010-07-22','2010-08-11',
'2010-09-01','2010-09-08','2010-09-21','2010-09-22','2010-10-01','2010-10-13','2010-10-15','2010-10-18','2010-10-20','2010-12-21','2010-12-22','2010-11-08','2010-11-17','2010-11-24','2010-11-26','2010-11-29','2010-12-06','2010-12-07','2010-12-14','2010-12-17',
'2011-01-10','2011-01-13','2011-02-02','2011-02-04','2011-02-14','2011-02-21','2011-02-24','2011-03-04','2011-03-22']
df.shape

df['text'] = [y1006a,y1006b,y1006c,y1007a,y1007b,y1008,y1009a,y1009b,y1009c,y1009d,y1010a,y1010b,y1010c,y1010d,y1010e,y1010f,y1010g,y1011a,y1011b,y1011c,y1011d,y1011e,y1012a,y1012b,y1012c,y1012d,
y1101a,y1101b,y1102a,y1102b,y1102c,y1102d,y1102e,y1103a,y1103b]

df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_tri3'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()