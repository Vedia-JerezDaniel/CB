with open('r200609.txt', encoding="utf8") as f:
     y2006a = f.read()
with open('r200615.txt', encoding="utf8") as f:
     y2006b= f.read()
with open('r200717.txt', encoding="utf8") as f:
     y2007 = f.read()
with open('r200910.txt', encoding="utf8") as f:
     y2009a = f.read()
with open('r200911.txt', encoding="utf8") as f:
     y2009b = f.read()
with open('r200914.txt', encoding="utf8") as f:
     y2009c = f.read()
with open('r200921.txt', encoding="utf8") as f:
     y2009d = f.read()
with open('r200929.txt', encoding="utf8") as f:
     y2009e = f.read()
with open('r200930.txt', encoding="utf8") as f:
     y2009f = f.read()

with open('r201019.txt', encoding="utf8") as f:
     y2010a = f.read()
with open('r201029.txt', encoding="utf8") as f:
     y2010b = f.read()
with open('r201113.txt', encoding="utf8") as f:
     y2011a = f.read()
with open('r201119.txt', encoding="utf8") as f:
     y2011b = f.read()
with open('r201120.txt', encoding="utf8") as f:
     y2011c = f.read()
with open('r201211.txt', encoding="utf8") as f:
     y2012 = f.read()

with open('r210121.txt', encoding="utf8") as f:
     y2101a = f.read()     
with open('r210127.txt', encoding="utf8") as f:
     y2101b = f.read()  
with open('r210211.txt', encoding="utf8") as f:
     y2102 = f.read()  

import pandas as pd
df = pd.DataFrame()

df['date'] = [
'2020-06-08','2020-06-15','2020-07-17','2020-09-10','2020-09-11','2020-09-04','2020-09-21','2020-09-29','2020-09-30','2020-10-19','2020-10-29','2020-11-13','2020-11-19','2020-11-20','2020-12-11',
'2021-01-21','2021-01-27','2021-02-11']
df.shape

df['text'] = [
y2006a,y2006b,y2007,y2009a,y2009b,y2009c,y2009d,y2009e,y2009f,y2010a,y2010b,y2011a,y2011b,y2011c,y2012,
y2101a,y2101b,y2102]  
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_lag2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()