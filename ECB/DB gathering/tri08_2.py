
with open('140408.txt', encoding="utf8") as f:
     y0804 = f.read()
with open('141008.txt', encoding="utf8") as f:
     y0810 = f.read()
with open('141108.txt', encoding="utf8") as f:
     y0811 = f.read()
with open('150208.txt', encoding="utf8") as f:
     y0802 = f.read()
with open('150408.txt', encoding="utf8") as f:
     y0804_1 = f.read()
with open('150508.txt', encoding="utf8") as f:
     y0805 = f.read()
with open('150908.txt', encoding="utf8") as f:
     y0809 = f.read()
with open('151208.txt', encoding="utf8") as f:
     y0812 = f.read()
with open('152008.txt', encoding="utf8") as f:
     y0805_1 = f.read()
with open('160108.txt', encoding="utf8") as f:
     y0801 = f.read()
with open('160508.txt', encoding="utf8") as f:
     y0805_2 = f.read()
with open('170108.txt', encoding="utf8") as f:
     y0801_1 = f.read()

with open('180108.txt', encoding="utf8") as f:
     y0801_2 = f.read()
with open('181108.txt', encoding="utf8") as f:
     y0811_1 = f.read()
with open('210908.txt', encoding="utf8") as f:
     y0809_1 = f.read()
with open('211108.txt', encoding="utf8") as f:
     y0811_2 = f.read()
with open('230108.txt', encoding="utf8") as f:
     y0801_3 = f.read()
with open('242008.txt', encoding="utf8") as f:
     y0804_2 = f.read()
with open('250208.txt', encoding="utf8") as f:
     y0802_1 = f.read()
with open('250408.txt', encoding="utf8") as f:
     y0804_3 = f.read()
with open('250608.txt', encoding="utf8") as f:
     y0806 = f.read()
with open('260308.txt', encoding="utf8") as f:
     y0803 = f.read()
with open('271008.txt', encoding="utf8") as f:
     y0810_1 = f.read()

with open('280208.txt', encoding="utf8") as f:
     y0802_2 = f.read()
with open('292008.txt', encoding="utf8") as f:
     y0809_2 = f.read()
with open('300408.txt', encoding="utf8") as f:
     y0804_4 = f.read()
with open('300908.txt', encoding="utf8") as f:
     y0809_3 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2008-04-14','2008-10-14','2008-11-14','2008-02-15','2008-04-15','2008-05-15','2008-09-15','2008-12-15','2008-05-12','2008-01-16','2008-10-16','2008-01-17','2008-01-18','2008-11-18','2008-09-21','2008-11-21','2008-01-23','2008-04-22','2008-02-25','2008-04-25','2008-06-25','2008-03-26','2008-10-27','2008-02-28','2008-04-28','2008-09-22','2008-04-30','2008-09-30']

df['text'] = [y0804, y0810, y0811, y0802, y0804_1, y0805, y0809, y0812, y0805_1, y0801, y0805_2, y0805, y0801_1, y0801_2, y0811_1, y0809_1, y0811_2, y0801_3, y0804_2, y0802_1, y0804_3, y0806, y0803, y0810_1, y0802_2, y0809_2, y0804_4, y0809_3]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle

db = 'df_tri08_1'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()