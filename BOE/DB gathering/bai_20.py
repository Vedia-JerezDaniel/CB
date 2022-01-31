with open('r210205.txt', encoding="utf8") as f:
     y2102 = f.read()
with open('r210211.txt', encoding="utf8") as f:
     y2102a = f.read()
with open('r210310.txt', encoding="utf8") as f:
     y2103 = f.read()
with open('r210326.txt', encoding="utf8") as f:
     y2103a = f.read()
with open('r210422.txt', encoding="utf8") as f:
     y2104 = f.read()
with open('r210512.txt', encoding="utf8") as f:
     y2105 = f.read()
with open('r210512a.txt', encoding="utf8") as f:
     y2105a = f.read()
with open('r210602.txt', encoding="utf8") as f:
     y2106 = f.read()
with open('r210604.txt', encoding="utf8") as f:
     y2106a = f.read()
with open('r210615.txt', encoding="utf8") as f:
     y2106b = f.read()
with open('r210702.txt', encoding="utf8") as f:
     y2107 = f.read()
with open('r210928.txt', encoding="utf8") as f:
     y2109 = f.read()
with open('r211105.txt', encoding="utf8") as f:
     y2111 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2021-02-05','2021-02-11','2021-03-10','2021-03-26','2021-04-18','2021-05-12','2021-05-13','2021-06-03','2021-06-04','2021-06-15','2021-07-02','2021-09-28','2021-11-04']
df['text'] = [y2102, y2102a, y2103, y2103a, y2104, y2105, y2105a, y2106, y2106a, y2106b, y2107, y2109, y2111]
df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_bailey20'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()
