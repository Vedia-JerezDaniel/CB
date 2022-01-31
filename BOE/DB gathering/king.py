# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:24:56 2021

@author: Sabine
"""
### ALL KING SPEECHES

with open('r090319a.txt', encoding="utf8") as f:
     y0903 = f.read()
with open('r090619b.txt', encoding="utf8") as f:
     y0906 = f.read()
with open('r091022a.txt', encoding="utf8") as f:
     y0910 = f.read()
with open('r100122a.txt', encoding="utf8") as f:
     y1001 = f.read()
with open('r100326a.txt', encoding="utf8") as f:
     y1003 = f.read()
with open('r100621b.txt', encoding="utf8") as f:
     y1006 = f.read()
with open('r100917b.txt', encoding="utf8") as f:
     y1009 = f.read()
with open('r101021a.txt', encoding="utf8") as f:
     y1010a = f.read()
with open('r101028a.txt', encoding="utf8") as f:
     y1010b = f.read()
with open('r110315a.txt', encoding="utf8") as f:
     y1103 = f.read()
with open('r110617c.txt', encoding="utf8") as f:
     y1106 = f.read()
with open('r111019e.txt', encoding="utf8") as f:
     y1110 = f.read()
with open('r120503c.txt', encoding="utf8") as f:
     y1205 = f.read()
with open('r121010f.txt', encoding="utf8") as f:
     y1212 = f.read()
with open('r130123c.txt', encoding="utf8") as f:
     y1301 = f.read()
with open('r130417c.txt', encoding="utf8") as f:
     y1304 = f.read()
with open('r130621a.txt', encoding="utf8") as f:
     y1306 = f.read()
         
import pandas as pd

df = pd.DataFrame()

df['date'] = ['2009-03-19','2009-06-19','2009-10-22','2010-01-22','2010-03-26','2010-06-21','2010-09-17','2010-10-21','2010-10-28','2011-03-15','2011-06-17','2011-10-19','2012-05-13','2012-12-25','2013-01-23','2013-04-17','2013-06-21']

df['text'] = [y0903, y0906, y0910, y1001, y1003, y1006, y1009, y1010a, y1010b, y1103, y1106, y1110, y1205, y1212, y1301, y1304, y1306]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_king'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()


lis = 'list_sent'
lis_o = open(lis,'wb')
pickle.dump(lmdict, lis_o)
lis_o.close()

# save a pickle
neg = 'negate'
neg_o = open(neg,'wb')
pickle.dump(negate, neg_o)
neg_o.close()

# recover a pickle
infile = open(neg,'rb')
negate = pickle.load(infile)
infile.close()
print(negate)
