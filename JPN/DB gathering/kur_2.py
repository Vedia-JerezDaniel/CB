with open('150724.txt', encoding="utf8") as f:
    y1507 = f.read()
with open('150828.txt', encoding="utf8") as f:
    y1508 = f.read()
with open('150929.txt', encoding="utf8") as f:
    y1509 = f.read()
with open('151110.txt', encoding="utf8") as f:
    y1511 = f.read()
with open('151207.txt', encoding="utf8") as f:
    y1512a = f.read()
with open('151210.txt', encoding="utf8") as f:
    y1512b = f.read()

with open('160204.txt', encoding="utf8") as f:
     y1602a = f.read()
with open('160218.txt', encoding="utf8") as f:
     y1602b = f.read()
with open('160307.txt', encoding="utf8") as f:
     y1603a = f.read()
with open('160317.txt', encoding="utf8") as f:
     y1603b = f.read()
with open('160418.txt', encoding="utf8") as f:
     y1604 = f.read()
with open('160518.txt', encoding="utf8") as f:
     y1605 = f.read()
with open('160623.txt', encoding="utf8") as f:
     y1606 = f.read()
with open('160823.txt', encoding="utf8") as f:
     y1608a = f.read()
with open('160831.txt', encoding="utf8") as f:
     y1608b = f.read()
with open('160908.txt', encoding="utf8") as f:
     y1609a = f.read()
with open('160928.txt', encoding="utf8") as f:
     y1609b = f.read()
with open('161004.txt', encoding="utf8") as f:
     y1610a = f.read()
with open('161021.txt', encoding="utf8") as f:
     y1610b = f.read()
with open('161114.txt', encoding="utf8") as f:
     y1611 = f.read()
with open('161206.txt', encoding="utf8") as f:
     y1612a = f.read()
with open('161214.txt', encoding="utf8") as f:
     y1612b = f.read()

with open('170106.txt', encoding="utf8") as f:
     y1701 = f.read()
with open('170215.txt', encoding="utf8") as f:
     y1702 = f.read()
with open('170313.txt', encoding="utf8") as f:
     y1703a = f.read()
with open('170324.txt', encoding="utf8") as f:
     y1703b = f.read()
with open('170418.txt', encoding="utf8") as f:
     y1704 = f.read()
with open('170503.txt', encoding="utf8") as f:
     y1705a = f.read()
with open('170509.txt', encoding="utf8") as f:
     y1705b = f.read()
with open('170510.txt', encoding="utf8") as f:
     y1705c = f.read()
with open('170522.txt', encoding="utf8") as f:
     y1705d = f.read()
with open('170601.txt', encoding="utf8") as f:
     y1706a = f.read()
with open('170608.txt', encoding="utf8") as f:
     y1706b = f.read()
with open('170612.txt', encoding="utf8") as f:
     y1706c = f.read()
with open('170926.txt', encoding="utf8") as f:
     y1709 = f.read()

import pandas as pd
df = pd.DataFrame()

df['date'] = ['2015-07-26','2015-08-23','2015-09-24','2015-11-10','2015-12-07','2015-12-18',
'2016-02-04','2016-02-18','2016-03-07','2016-03-17','2016-04-18','2016-05-25','2016-06-23','2016-08-23','2016-08-31','2016-09-08','2016-09-29','2016-10-04','2016-10-29','2016-11-12','2016-12-06','2016-12-14',
'2017-01-04','2017-02-18','2017-03-13','2017-03-24','2017-04-18','2017-05-03','2017-05-09','2017-05-10','2017-05-22','2017-06-01','2017-06-08','2017-06-12','2017-09-29']
df.shape

df['text'] = [y1507,y1508,y1509,y1511,y1512a,y1512b,
y1602a,y1602b,y1603a,y1603b,y1604,y1605,y1606,y1608a,y1608b,y1609a,y1609b,y1610a,y1610b,y1611,y1612a,y1612b,
y1701,y1702,y1703a,y1703b,y1704,y1705a,y1705b,y1705c,y1705d,y1706a,y1706b,y1706c,y1709]
df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_kur2'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()