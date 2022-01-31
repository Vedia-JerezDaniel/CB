### CARNEY ONE SPEECHES

with open('r160126.txt', encoding="utf8") as f:
     y1601 = f.read()
with open('r160229.txt', encoding="utf8") as f:
     y1602 = f.read()
with open('r160405.txt', encoding="utf8") as f:
     y1604 = f.read()
with open('r160523.txt', encoding="utf8") as f:
     y1605a = f.read()
with open('r160531.txt', encoding="utf8") as f:
     y1605b = f.read()
with open('r160607.txt', encoding="utf8") as f:
     y1606a = f.read()
with open('r160621.txt', encoding="utf8") as f:
     y1606b = f.read()
with open('r160704.txt', encoding="utf8") as f:
     y1607 = f.read()
with open('r160926.txt', encoding="utf8") as f:
     y1609 = f.read()
with open('r161207.txt', encoding="utf8") as f:
     y1612a = f.read()
with open('r161216.txt', encoding="utf8") as f:
     y1612b = f.read()
with open('r170118.txt', encoding="utf8") as f:
     y1701a = f.read()
with open('r170126.txt', encoding="utf8") as f:
     y1701b = f.read()
with open('r170210.txt', encoding="utf8") as f:
     y1702 = f.read()     
with open('r170322.txt', encoding="utf8") as f:
     y1703 = f.read()
with open('r170420.txt', encoding="utf8") as f:
     y1704a = f.read()
with open('r170424.txt', encoding="utf8") as f:
     y1704b = f.read()
with open('r170428.txt', encoding="utf8") as f:
     y1704c = f.read()
with open('r170628.txt', encoding="utf8") as f:
     y1706 = f.read()
with open('r170711.txt', encoding="utf8") as f:
     y1707a = f.read()
with open('r170724.txt', encoding="utf8") as f:
     y1707b = f.read()
with open('r170920.txt', encoding="utf8") as f:
     y1709a = f.read()
with open('r170928.txt', encoding="utf8") as f:
     y1709b = f.read()
with open('r171205.txt', encoding="utf8") as f:
     y1712a = f.read()
with open('r171219.txt', encoding="utf8") as f:
     y1712b = f.read()
with open('r180220.txt', encoding="utf8") as f:
     y1802 = f.read()
with open('r180323.txt', encoding="utf8") as f:
     y1803 = f.read()



import pandas as pd
df = pd.DataFrame()

df['date'] = ['2016-01-25','2016-02-29','2016-04-05','2016-05-23','2016-05-31','2016-06-07','2016-06-21','2016-07-04','2016-09-28','2016-12-07','2016-12-16',
'2017-01-18','2017-01-26','2017-02-15','2017-03-22','2017-04-20','2017-04-27','2017-04-28','2017-06-27','2017-07-11','2017-07-24','2017-09-20','2017-09-28','2017-12-05','2017-12-19',
'2018-02-20','2018-03-23']

df['text'] = [y1601,y1602,y1604,y1605a,y1605b,y1606a,y1606b,y1607,y1609,y1612a,y1612b,    
y1701a,y1701b,y1702,y1703,y1704a,y1704b,y1704c,y1706,y1707a,y1707b,y1709a,y1709b,y1712a,y1712b,
y1802,y1803]

df.head()

df['ntex'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_car2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()