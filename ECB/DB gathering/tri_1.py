### TRICHET ONE SPEECHES

with open('r090210.txt', encoding="utf8") as f:
     y0902a = f.read()
with open('r090217.txt', encoding="utf8") as f:
     y0902b = f.read()
with open('r090218.txt', encoding="utf8") as f:
     y0902c = f.read()
with open('r090224.txt', encoding="utf8") as f:
     y0902d = f.read()
with open('r090226.txt', encoding="utf8") as f:
     y0902e = f.read()

with open('r090303.txt', encoding="utf8") as f:
     y0903a = f.read()
with open('r090309.txt', encoding="utf8") as f:
     y0903b = f.read()
with open('r090317.txt', encoding="utf8") as f:
     y0903c = f.read()
with open('r090318.txt', encoding="utf8") as f:
     y0903d = f.read()
with open('r090401.txt', encoding="utf8") as f:
     y0904a = f.read()
with open('r090403.txt', encoding="utf8") as f:
     y0904b = f.read()
with open('r090422.txt', encoding="utf8") as f:
     y0904c = f.read()
with open('r090423.txt', encoding="utf8") as f:
     y0904d = f.read()
with open('r090428.txt', encoding="utf8") as f:
     y0904e = f.read()     
with open('r090508.txt', encoding="utf8") as f:
     y0905a = f.read()
with open('r090529.txt', encoding="utf8") as f:
     y0905b = f.read()
with open('r090603.txt', encoding="utf8") as f:
     y0906a = f.read()
with open('r090609.txt', encoding="utf8") as f:
     y0906b = f.read()
with open('r090611.txt', encoding="utf8") as f:
     y0906c = f.read()
with open('r090617.txt', encoding="utf8") as f:
     y0906d = f.read()
with open('r090619.txt', encoding="utf8") as f:
     y0906e = f.read()
with open('r090624.txt', encoding="utf8") as f:
     y0906f = f.read()
with open('r090708.txt', encoding="utf8") as f:
     y0907a = f.read()
with open('r090715.txt', encoding="utf8") as f:
     y0907b = f.read()
with open('r090721.txt', encoding="utf8") as f:
     y0907c = f.read()
with open('r090811.txt', encoding="utf8") as f:
     y0908a = f.read()
with open('r090828.txt', encoding="utf8") as f:
     y0908b = f.read()
with open('r090907.txt', encoding="utf8") as f:
     y0909a = f.read()
with open('r090908.txt', encoding="utf8") as f:
     y0909b = f.read()
with open('r091001.txt', encoding="utf8") as f:
     y0910a = f.read()
with open('r091007.txt', encoding="utf8") as f:
     y0910b = f.read()
with open('r091008.txt', encoding="utf8") as f:
     y0910c = f.read()
with open('r091012.txt', encoding="utf8") as f:
     y0910d = f.read()
with open('r091014.txt', encoding="utf8") as f:
     y0910e = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2009-02-10','2009-02-17','2009-02-18','2009-02-24','2009-02-26','2009-03-03',
'2009-03-09','2009-03-17','2009-03-18','2009-04-01','2009-04-03','2009-04-22','2009-04-23','2009-04-28','2009-05-08','2009-05-29','2009-06-03','2009-06-09','2009-06-11','2009-06-17','2009-06-19','2009-06-24',
'2009-07-08','2009-07-15','2009-07-21','2009-08-11','2009-08-28','2009-09-07','2009-09-08','2009-10-01','2009-10-07','2009-10-08','2009-10-12','2009-10-15']
df.shape

df['text'] = [y0902a,y0902b,y0902c,y0902d,y0902e,y0903a,y0903b,y0903c,y0903d,y0904a,y0904b,y0904c,y0904d,y0904e,
y0905a,y0905b,y0906a,y0906b,y0906c,y0906d,y0906e,y0906f,y0907a,y0907b,y0907c,y0908a,y0908b,y0909a,y0909b,
y0910a,y0910b,y0910c,y0910d,y0910e]

df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_tri1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()