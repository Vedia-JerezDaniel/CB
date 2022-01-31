with open('r110324.txt', encoding="utf8") as f:
     y1103 = f.read()
with open('r110406.txt', encoding="utf8") as f:
     y1104a = f.read()
with open('r110408.txt', encoding="utf8") as f:
     y1104b = f.read()
with open('r110503.txt', encoding="utf8") as f:
     y1105a = f.read()
with open('r110509.txt', encoding="utf8") as f:
     y1105b = f.read()
with open('r110530.txt', encoding="utf8") as f:
     y1105c = f.read()
with open('r110607.txt', encoding="utf8") as f:
     y1106a = f.read()
with open('r110608.txt', encoding="utf8") as f:
     y1106b = f.read()
with open('r110614.txt', encoding="utf8") as f:
     y1106c = f.read()
with open('r110615.txt', encoding="utf8") as f:
     y1106d = f.read()
with open('r110621.txt', encoding="utf8") as f:
     y1106e = f.read()
with open('r110630.txt', encoding="utf8") as f:
     y1106f = f.read()

with open('r110704.txt', encoding="utf8") as f:
     y1107a = f.read()
with open('r110711.txt', encoding="utf8") as f:
     y1107b = f.read()
with open('r110809.txt', encoding="utf8") as f:
     y1108a = f.read()
with open('r110829.txt', encoding="utf8") as f:
     y1108b = f.read()     
with open('r110830.txt', encoding="utf8") as f:
     y1108c = f.read()
with open('r110909.txt', encoding="utf8") as f:
     y1109a = f.read()
with open('r110920.txt', encoding="utf8") as f:
     y1109b = f.read()
with open('r110926.txt', encoding="utf8") as f:
     y1109c = f.read()
with open('r111006.txt', encoding="utf8") as f:
     y1110a = f.read()
with open('r111021.txt', encoding="utf8") as f:
     y1110b = f.read()
with open('r111024.txt', encoding="utf8") as f:
     y1110c = f.read()
with open('r111025.txt', encoding="utf8") as f:
     y1110d = f.read()
with open('r111102.txt', encoding="utf8") as f:
     y1111 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2011-03-24','2011-04-06','2011-04-08','2011-05-03','2011-05-09','2011-05-30','2011-06-07','2011-06-08','2011-06-14','2011-06-15','2011-06-21','2011-06-30','2011-07-04','2011-07-11','2011-08-09','2011-08-29','2011-08-30',
'2011-09-09','2011-09-20','2011-09-26','2011-10-06','2011-10-21','2011-10-24','2011-10-25','2011-11-02',]
df.shape

df['text'] = [y1103,y1104a,y1104b,y1105a,y1105b,y1105c,y1106a,y1106b,y1106c,y1106d,y1106e,y1106f,y1107a,y1107b,y1108a, y1108b,y1108c,y1109a,y1109b,y1109c,y1110a,y1110b,y1110c,y1110d,y1111]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_tri4'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()