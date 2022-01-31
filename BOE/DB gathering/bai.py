### ALL BAILEY SPEECHES

with open('r200717.txt', encoding="utf8") as f:
     y2007 = f.read()
with open('r200901.txt', encoding="utf8") as f:
     y2009a = f.read()
with open('r200903.txt', encoding="utf8") as f:
     y2009b = f.read()
with open('r201109.txt', encoding="utf8") as f:
     y2011a = f.read()
with open('r201118.txt', encoding="utf8") as f:
     y2011b = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2020-07-17','2020-09-01','2020-09-03','2020-11-09','2020-11-18']

df['text'] = [y2007, y2009a, y2009b, y2011a, y2011b]

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_bailey'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()
