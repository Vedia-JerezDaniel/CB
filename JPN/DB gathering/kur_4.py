with open('200803.txt', encoding="utf8") as f:
     y2008 = f.read()
with open('200923.txt', encoding="utf8") as f:
     y2009 = f.read()
with open('201007.txt', encoding="utf8") as f:
     y2010 = f.read()
with open('201104.txt', encoding="utf8") as f:
     y2011a = f.read()
with open('201125.txt', encoding="utf8") as f:
     y2011b = f.read()
with open('201223.txt', encoding="utf8") as f:
     y2012a = f.read()   
with open('201228.txt', encoding="utf8") as f:
     y2012b = f.read()  


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2020-08-09','2020-09-23','2020-10-07','2020-11-04','2020-11-26','2020-12-23','2020-12-28']
df.shape

df['text'] = [y2008,y2009,y2010,y2011a,y2011b,y2012a,y2012b]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_kur4'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()