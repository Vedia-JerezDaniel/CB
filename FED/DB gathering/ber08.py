with open('011008.txt', encoding="utf8") as f:
     y0801 = f.read()
with open('030408.txt', encoding="utf8") as f:
     y0803 = f.read()
with open('031408.txt', encoding="utf8") as f:
     y0803_1 = f.read()
with open('040908.txt', encoding="utf8") as f:
     y0804 = f.read()
with open('041008.txt', encoding="utf8") as f:
     y0804_1 = f.read()
with open('050508.txt', encoding="utf8") as f:
     y0805 = f.read()
with open('051308.txt', encoding="utf8") as f:
     y0805_1 = f.read()
with open('051508.txt', encoding="utf8") as f:
     y0805_2 = f.read()

with open('060308.txt', encoding="utf8") as f:
     y0806 = f.read()
with open('060408.txt', encoding="utf8") as f:
     y0806_1 = f.read()
with open('060908.txt', encoding="utf8") as f:
     y0806_2 = f.read()
with open('061208.txt', encoding="utf8") as f:
     y0806_3 = f.read()
with open('061608.txt', encoding="utf8") as f:
     y0806_4 = f.read()
with open('070808.txt', encoding="utf8") as f:
     y0807 = f.read()
with open('082208.txt', encoding="utf8") as f:
     y0808 = f.read()
with open('101408.txt', encoding="utf8") as f:
     y0810 = f.read()
with open('101508.txt', encoding="utf8") as f:
     y0810_1 = f.read()
with open('103108.txt', encoding="utf8") as f:
     y0810_2 = f.read()
    
with open('111408.txt', encoding="utf8") as f:
     y0811 = f.read()
with open('112008.txt', encoding="utf8") as f:
     y0812 = f.read()
with open('142008.txt', encoding="utf8") as f:
     y0812_1 = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2008-01-10','2008-03-04','2008-03-14','2008-04-09','2008-04-10','2008-05-05','2008-05-13','2008-05-15','2008-06-03','2008-06-04','2008-06-09','2008-06-12','2008-06-16','2008-07-08','2008-08-22','2008-10-14','2008-10-15','2008-10-31','2008-11-14','2008-12-01','2008-12-04']

df['text'] = [y0801, y0803, y0803_1, y0804, y0804_1, y0805, y0805_1, y0805_2, y0806, y0806_1, y0806_2, y0806_3, y0806_4, y0807, y0808, y0810, y0810_1, y0810_2, y0811, y0812, y0812_1]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle

db = 'df_ber08'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()