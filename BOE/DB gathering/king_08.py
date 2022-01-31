

with open('042008.txt', encoding="utf8") as f:
     y0804 = f.read()
with open('140308.txt', encoding="utf8") as f:
     y0803 = f.read()
with open('210608.txt', encoding="utf8") as f:
     y0806 = f.read()
with open('262008.txt', encoding="utf8") as f:
     y0801 = f.read()
with open('281008.txt', encoding="utf8") as f:
     y0810 = f.read()
with open('310308.txt', encoding="utf8") as f:
     y0803_1 = f.read()


import pandas as pd

df = pd.DataFrame()

df['date'] = ['2008-04-20','2008-03-19','2008-06-21','2008-01-22','2008-10-28','2008-03-31']

df['text'] = [y0804, y0803, y0806, y0801, y0810, y0803_1]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle

db = 'df_king08'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()
