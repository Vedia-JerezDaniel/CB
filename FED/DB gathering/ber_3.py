with open('r110421.txt', encoding="utf8") as f:
     y1104 = f.read()
with open('r110502.txt', encoding="utf8") as f:
     y1105a = f.read()
with open('r110509.txt', encoding="utf8") as f:
     y1105b = f.read()
with open('r110512.txt', encoding="utf8") as f:
     y1105c = f.read()
with open('r110513.txt', encoding="utf8") as f:
     y1105d = f.read()
with open('r110518.txt', encoding="utf8") as f:
     y1105e = f.read()
with open('r110608.txt', encoding="utf8") as f:
     y1106a = f.read()
with open('r110615.txt', encoding="utf8") as f:
     y1106b = f.read()
with open('r110719.txt', encoding="utf8") as f:
     y1107a = f.read()
with open('r110722.txt', encoding="utf8") as f:
     y1107b = f.read()
with open('r110826.txt', encoding="utf8") as f:
     y1108 = f.read()
with open('r110909.txt', encoding="utf8") as f:
     y1109a = f.read()
with open('r110916.txt', encoding="utf8") as f:
     y1109b = f.read()
with open('r110929.txt', encoding="utf8") as f:
     y1109c = f.read()     
with open('r111005.txt', encoding="utf8") as f:
     y1110a= f.read()
with open('r111019.txt', encoding="utf8") as f:
     y1110b = f.read()
with open('r111110.txt', encoding="utf8") as f:
     y1111a = f.read()
with open('r111111.txt', encoding="utf8") as f:
     y1111b = f.read()

with open('r120203.txt', encoding="utf8") as f:
     y1202a = f.read()
with open('r120220.txt', encoding="utf8") as f:
     y1202b = f.read()
with open('r120301.txt', encoding="utf8") as f:
     y1203a = f.read()
with open('r120315.txt', encoding="utf8") as f:
     y1203b = f.read()
with open('r120321.txt', encoding="utf8") as f:
     y1203c = f.read()
with open('r120327.txt', encoding="utf8") as f:
     y1203d = f.read()
with open('r120410.txt', encoding="utf8") as f:
     y1204a = f.read()
with open('r120416.txt', encoding="utf8") as f:
     y1204b = f.read()
with open('r120511.txt', encoding="utf8") as f:
     y1205 = f.read()
with open('r120608.txt', encoding="utf8") as f:
     y1206 = f.read()
with open('r120718.txt', encoding="utf8") as f:
     y1207a = f.read()
with open('r120727.txt', encoding="utf8") as f:
     y1207b = f.read()
with open('r120807.txt', encoding="utf8") as f:
     y1208a = f.read()
with open('r120808.txt', encoding="utf8") as f:
     y1208b = f.read()
with open('r120903.txt', encoding="utf8") as f:
     y1209 = f.read()
with open('r121002.txt', encoding="utf8") as f:
     y1210 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2011-04-21','2011-05-02','2011-05-09','2011-05-12','2011-05-13','2011-05-18','2011-06-08','2011-06-17','2011-07-19','2011-07-22','2011-08-26','2011-09-09','2011-09-16','2011-09-29','2011-10-05','2011-10-19','2011-11-10','2011-11-11',
'2012-02-03','2012-02-20','2012-03-01','2012-03-15','2012-03-21','2012-03-27','2012-04-10','2012-10-16','2012-05-17',
'2012-06-10','2012-07-13','2012-07-28','2012-08-07','2012-08-08','2012-09-03','2012-10-02']
df.shape

df['text'] = [y1104,y1105a,y1105b,y1105c,y1105d,y1105e,y1106a,y1106b,y1107a,y1107b,y1108,y1109a,y1109b,y1109c,y1110a,y1110b,y1111a,y1111b,
y1202a,y1202b,y1203a,y1203b,y1203c,y1203d,y1204a,y1204b,y1205,y1206,y1207a,y1207b,y1208a,y1208b,y1209,y1210]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_ber3'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()