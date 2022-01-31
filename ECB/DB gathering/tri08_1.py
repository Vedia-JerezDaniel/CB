with open('30408.txt', encoding="utf8") as f:
     y0804 = f.read()
with open('30608.txt', encoding="utf8") as f:
     y0806 = f.read()
with open('30708.txt', encoding="utf8") as f:
     y0807 = f.read()
with open('40608.txt', encoding="utf8") as f:
     y0806_1 = f.read()
with open('50108.txt', encoding="utf8") as f:
     y0801 = f.read()
with open('50908.txt', encoding="utf8") as f:
     y0809 = f.read()
with open('60508.txt', encoding="utf8") as f:
     y0805 = f.read()
with open('62008.txt', encoding="utf8") as f:
     y0806_2 = f.read()
with open('70308.txt', encoding="utf8") as f:
     y0803 = f.read()
with open('81208.txt', encoding="utf8") as f:
     y0812 = f.read()
with open('90708.txt', encoding="utf8") as f:
     y0807_1 = f.read()

with open('100708.txt', encoding="utf8") as f:
     y0807_2 = f.read()
with open('100908.txt', encoding="utf8") as f:
     y0809_1 = f.read()
with open('110908.txt', encoding="utf8") as f:
     y0809_2 = f.read()
with open('111208.txt', encoding="utf8") as f:
     y0812 = f.read()
with open('112008.txt', encoding="utf8") as f:
     y0801_1 = f.read()
with open('121108.txt', encoding="utf8") as f:
     y0811 = f.read()
with open('130208.txt', encoding="utf8") as f:
     y0802 = f.read()
with open('131108.txt', encoding="utf8") as f:
     y0811_1 = f.read()
with open('140208.txt', encoding="utf8") as f:
     y0802_1 = f.read()


import pandas as pd

df = pd.DataFrame()

df['date'] = ['2008-04-03','2008-06-03','2008-07-30','2008-06-04','2008-01-05','2008-09-05','2008-05-06','2008-06-20','2008-03-07','2008-12-08','2008-07-09','2008-07-10','2008-09-10','2008-09-11','2008-12-11','2008-01-12','2008-11-12','2008-02-13','2008-11-13','2008-02-14']

df['text'] = [y0804, y0806, y0807, y0806_1, y0801, y0809, y0805, y0806_2, y0803, y0812, y0807_1, y0807_2, y0809_1, y0809_2, y0812, y0801_1, y0811, y0802, y0811_1, y0802_1]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle

db = 'df_tri08'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()
