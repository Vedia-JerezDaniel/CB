
with open('06408.txt', encoding="utf8") as f:
     y0806 = f.read()
with open('09208.txt', encoding="utf8") as f:
     y0809 = f.read()
with open('11508.txt', encoding="utf8") as f:
     y0811 = f.read()
with open('12108.txt', encoding="utf8") as f:
     y0812 = f.read()
with open('052208.txt', encoding="utf8") as f:
     y0805 = f.read()
with open('052308.txt', encoding="utf8") as f:
     y0805_1 = f.read()
with open('052808.txt', encoding="utf8") as f:
     y0805_2 = f.read()
with open('071808.txt', encoding="utf8") as f:
     y0807 = f.read()
with open('082508.txt', encoding="utf8") as f:
     y0808 = f.read()
with open('112608.txt', encoding="utf8") as f:
     y0811 = f.read()
with open('121608.txt', encoding="utf8") as f:
     y0812 = f.read()
with open('122208.txt', encoding="utf8") as f:
     y0812_1 = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2008-06-04','2008-09-02','2008-11-05','2008-12-01','2008-05-22','2008-05-23','2008-05-28','2008-07-18','2008-08-25','2008-11-26','2008-12-16','2008-12-22']
df['text'] = [y0806, y0809, y0811, y0812, y0805, y0805_1,y0805_2, y0807, y0808, y0811, y0812, y0812_1]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle

db = 'df_shi08'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()
