### DRAGUI ONE SPEECHES

with open('r111021.txt', encoding="utf8") as f:
     y1110a = f.read()
with open('r111027.txt', encoding="utf8") as f:
     y1110b = f.read()
with open('r111107.txt', encoding="utf8") as f:
     y1111a = f.read()
with open('r111121.txt', encoding="utf8") as f:
     y1111b = f.read()
with open('r111201.txt', encoding="utf8") as f:
     y1112a = f.read()
with open('r111221.txt', encoding="utf8") as f:
     y1112b = f.read()

with open('r120113.txt', encoding="utf8") as f:
     y1201 = f.read()
with open('r120210.txt', encoding="utf8") as f:
     y1202 = f.read()
with open('r120313.txt', encoding="utf8") as f:
     y1203a = f.read()
with open('r120315.txt', encoding="utf8") as f:
     y1203b = f.read()
with open('r120328.txt', encoding="utf8") as f:
     y1203c = f.read()
with open('r120405.txt', encoding="utf8") as f:
     y1204a = f.read()
with open('r120418.txt', encoding="utf8") as f:
     y1204b = f.read()
with open('r120426.txt', encoding="utf8") as f:
     y1204c = f.read()
with open('r120504.txt', encoding="utf8") as f:
     y1205a = f.read()     
with open('r120509.txt', encoding="utf8") as f:
     y1205b = f.read()
with open('r120521.txt', encoding="utf8") as f:
     y1205c = f.read()
with open('r120525.txt', encoding="utf8") as f:
     y1205d = f.read()
with open('r120607.txt', encoding="utf8") as f:
     y1206a = f.read()
with open('r120615.txt', encoding="utf8") as f:
     y1206b = f.read()

with open('r120710.txt', encoding="utf8") as f:
     y1207a = f.read()
with open('r120727.txt', encoding="utf8") as f:
     y1207b = f.read()
with open('r120803.txt', encoding="utf8") as f:
     y1208a = f.read()
with open('r120830.txt', encoding="utf8") as f:
     y1208b = f.read()
with open('r120907.txt', encoding="utf8") as f:
     y1209a = f.read()
with open('r120911.txt', encoding="utf8") as f:
     y1209b = f.read()
with open('r120917.txt', encoding="utf8") as f:
     y1209c = f.read()
with open('r120926.txt', encoding="utf8") as f:
     y1209d = f.read()
with open('r121005.txt', encoding="utf8") as f:
     y1210a = f.read()
with open('r121009.txt', encoding="utf8") as f:
     y1210b = f.read()
with open('r121015.txt', encoding="utf8") as f:
     y1210c = f.read()



import pandas as pd
df = pd.DataFrame()

df['date'] = ['2011-10-21','2011-10-27','2011-11-07','2011-11-21','2011-12-01','2011-12-21',
'2012-01-13','2012-02-10','2012-03-13','2012-03-15','2012-03-27','2012-04-05','2012-04-18','2012-04-26','2012-05-04','2012-05-09','2012-05-21','2012-05-25','2012-06-07','2012-06-15',
'2012-07-10','2012-07-27','2012-08-03','2012-08-30','2012-09-07','2012-09-11','2012-09-17','2012-09-26','2012-10-05','2012-10-09','2012-10-15']

df['text'] = [y1110a,y1110b,y1111a,y1111b,y1112a,y1112b,  
y1201,y1202,y1203a,y1203b,y1203c,y1204a,y1204b,y1204c,y1205a,y1205b,y1205c,y1205d,y1206a,y1206b,y1207a,y1207b,y1208a,y1208b,y1209a,y1209b,y1209c,y1209d,y1210a,y1210b,y1210c]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))
df.drop('text', axis=1, inplace=True)
df.rename({'ntex' : 'text'}, axis=1, inplace=True)

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_dra1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()