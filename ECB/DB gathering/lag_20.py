with open('r210302.txt', encoding="utf8") as f:
     y2103 = f.read()
with open('r210303.txt', encoding="utf8") as f:
     y2103a = f.read()
with open('r210311.txt', encoding="utf8") as f:
     y2103b = f.read()
with open('r210414.txt', encoding="utf8") as f:
     y2103c = f.read()
with open('r210414.txt', encoding="utf8") as f:
     y2104 = f.read()
with open('r210423.txt', encoding="utf8") as f:
     y2104a = f.read()
with open('r210506.txt', encoding="utf8") as f:
     y2105 = f.read()
with open('r210603.txt', encoding="utf8") as f:
     y2106 = f.read()
with open('r210610.txt', encoding="utf8") as f:
     y2106a = f.read()
with open('r210622.txt', encoding="utf8") as f:
     y2106b = f.read()
with open('r210702.txt', encoding="utf8") as f:
     y2107 = f.read()
with open('r210709.txt', encoding="utf8") as f:
     y2107a = f.read()
with open('r210712.txt', encoding="utf8") as f:
     y2107b = f.read()
with open('r210722.txt', encoding="utf8") as f:
     y2107c = f.read()
with open('r210928.txt', encoding="utf8") as f:
     y2109 = f.read()
with open('r211109.txt', encoding="utf8") as f:
     y2111 = f.read()
with open('r211115.txt', encoding="utf8") as f:
     y2111a = f.read()
with open('r211119.txt', encoding="utf8") as f:
     y2111b = f.read()
with open('r211126.txt', encoding="utf8") as f:
     y2111c = f.read()
with open('r211129.txt', encoding="utf8") as f:
     y2111d = f.read()
     
import pandas as pd
df = pd.DataFrame()

df['date'] = ['2021-03-02','2021-03-03','2021-03-11','2021-03-18','2021-04-14','2021-04-23','2021-05-07','2021-06-10','2021-06-03','2021-06-22','2021-07-02','2021-07-09','2021-07-12','2021-07-22','2021-09-28','2021-11-09','2021-11-16','2021-11-19','2021-11-26','2021-11-29']
df.shape

df['text'] = [y2103,y2103a,y2103b,y2103c, y2104,y2104a,y2105,y2106,y2106a,y2106b,y2107,y2107a, y2107b, y2107c, y2109, y2111,y2111a, y2111b, y2111c, y2111d]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_lag20'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()