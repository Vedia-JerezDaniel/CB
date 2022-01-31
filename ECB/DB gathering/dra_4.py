with open('r140926.txt', encoding="utf8") as f:
     y1409 = f.read()
with open('r141003.txt', encoding="utf8") as f:
     y1410a = f.read()
with open('r141014.txt', encoding="utf8") as f:
     y1410b = f.read()
with open('r141110.txt', encoding="utf8") as f:
     y1411a = f.read()
with open('r141113.txt', encoding="utf8") as f:
     y1411b = f.read()
with open('r141118.txt', encoding="utf8") as f:
     y1411c = f.read()
with open('r141121.txt', encoding="utf8") as f:
     y1411d = f.read()
with open('r141127.txt', encoding="utf8") as f:
     y1411e = f.read()
with open('r141205.txt', encoding="utf8") as f:
     y1412 = f.read()

with open('r150112.txt', encoding="utf8") as f:
     y1501a = f.read()
with open('r150115.txt', encoding="utf8") as f:
     y1501b = f.read()
with open('r150122.txt', encoding="utf8") as f:
     y1501c = f.read()
with open('r150225.txt', encoding="utf8") as f:
     y1502 = f.read()
with open('r150302.txt', encoding="utf8") as f:
     y1503a = f.read()
with open('r150305.txt', encoding="utf8") as f:
     y1503b = f.read()     
with open('r150313.txt', encoding="utf8") as f:
     y1503c = f.read()
with open('r150318.txt', encoding="utf8") as f:
     y1503d = f.read()
with open('r150324.txt', encoding="utf8") as f:
     y1503e = f.read()
with open('r150401.txt', encoding="utf8") as f:
     y1504a = f.read()
with open('r150408.txt', encoding="utf8") as f:
     y1504b = f.read()

# DRAGRI MISSING 15-05 TO 15-12

with open('r150519.txt', encoding="utf8") as f:
     y1505a = f.read()
with open('r150522.txt', encoding="utf8") as f:
     y1505b = f.read()
with open('r150604.txt', encoding="utf8") as f:
     y1506a = f.read()
with open('r150618.txt', encoding="utf8") as f:
     y1506b = f.read()
with open('r150717.txt', encoding="utf8") as f:
     y1507a = f.read()
with open('r150720.txt', encoding="utf8") as f:
     y1507b = f.read()     
with open('r150903.txt', encoding="utf8") as f:
     y1509a = f.read()
with open('r150925.txt', encoding="utf8") as f:
     y1509b = f.read()
with open('r151002.txt', encoding="utf8") as f:
     y1510a = f.read()
with open('r151012.txt', encoding="utf8") as f:
     y1510b = f.read()
with open('r151023.txt', encoding="utf8") as f:
     y1510c = f.read()
with open('r151103.txt', encoding="utf8") as f:
     y1511a = f.read()     
with open('r151109.txt', encoding="utf8") as f:
     y1511b = f.read()
with open('r151111.txt', encoding="utf8") as f:
     y1511c = f.read()
with open('r151113.txt', encoding="utf8") as f:
     y1511d = f.read()
with open('r151125.txt', encoding="utf8") as f:
     y1511e = f.read()
with open('r151204.txt', encoding="utf8") as f:
     y1512a = f.read()
with open('r151208.txt', encoding="utf8") as f:
     y1512b = f.read()
with open('r151214.txt', encoding="utf8") as f:
     y1512c = f.read()
with open('r151216.txt', encoding="utf8") as f:
     y1512d = f.read()

# IM DONE

with open('r160126.txt', encoding="utf8") as f:
     y1601 = f.read()
with open('r160202.txt', encoding="utf8") as f:
     y1602a = f.read()
with open('r160205.txt', encoding="utf8") as f:
     y1602b = f.read()
with open('r160217.txt', encoding="utf8") as f:
     y1602c = f.read()
with open('r160310.txt', encoding="utf8") as f:
     y1603 = f.read()
with open('r160408.txt', encoding="utf8") as f:
     y1604a = f.read()
with open('r160418.txt', encoding="utf8") as f:
     y1604b = f.read()
with open('r160422.txt', encoding="utf8") as f:
     y1604c = f.read()
with open('r160506.txt', encoding="utf8") as f:
     y1605 = f.read()
with open('r160607.txt', encoding="utf8") as f:
     y1606a = f.read()
with open('r160608.txt', encoding="utf8") as f:
     y1606b= f.read()
with open('r160609.txt', encoding="utf8") as f:
     y1606c = f.read()
with open('r160623.txt', encoding="utf8") as f:
     y1606d = f.read()
with open('r160629.txt', encoding="utf8") as f:
     y1606e= f.read()
with open('r160721.txt', encoding="utf8") as f:
     y1607 = f.read()
with open('r160908.txt', encoding="utf8") as f:
     y1609a = f.read()
with open('r160915.txt', encoding="utf8") as f:
     y1609b= f.read()
with open('r160926.txt', encoding="utf8") as f:
     y1609c = f.read()


import pandas as pd
df = pd.DataFrame()

df['date'] = ['2014-09-26','2014-10-03','2014-10-14','2014-11-10','2014-11-13','2014-11-18','2014-11-21','2014-11-27','2014-12-05',
'2015-01-12','2015-01-15','2015-01-22','2015-02-25','2015-03-02','2015-03-05','2015-03-13','2015-03-18','2015-03-24','2015-04-01','2015-04-08',
'2016-01-26','2016-02-02','2016-02-05','2016-02-17','2016-03-10','2016-04-08','2016-04-18','2016-04-22',
'2016-05-05','2016-06-07','2016-06-08','2016-06-09','2016-06-23','2016-06-29','2016-07-21','2016-09-08','2016-09-15','2016-09-26']

df.shape

df['text'] = [y1409,y1410a,y1410b,y1411a,y1411b,y1411c,y1411d,y1411e,y1412,
y1501a,y1501b,y1501c,y1502,y1503a,y1503b,y1503c,y1503d,y1503e,y1504a,y1504b,
y1601,y1602a,y1602b,y1602c,y1603,y1604a,y1604b,y1604c,y1605,y1606a,y1606b,y1606c,y1606d,y1606e,y1607,y1609a,y1609b,y1609c]

df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_dra4'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()

# MISSING PART

import pandas as pd
df = pd.DataFrame()

df['date'] = [
'2015-05-19','2015-05-22','2015-06-04','2015-06-18','2015-07-17','2015-07-20','2015-09-03','2015-09-25','2015-10-02','2015-10-12','2015-10-23','2015-11-03','2015-11-09','2015-11-11','2015-11-13','2015-11-25','2015-12-04','2015-12-08','2015-12-14','2015-12-16']

df.shape

df['text'] = [y1505a,y1505b,y1506a,y1506b,y1507a,y1507b,y1509a,y1509b,
y1510a,y1510b,y1510c,y1511a,y1511b,y1511c,y1511d,y1511e,y1512a,y1512b,y1512c,y1512d]

df.head()

df['text'] = df['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

#Dictionary tone assessment will compare them by Index (need the numbers back) 
df['Index'] = range(0, len(df))

# Make 'date' column as the index of df
df.set_index(['date'], inplace=True)
df.head()

import re
import pickle
db = 'df_dra41'
db_o = open(db,'wb')
pickle.dump(df,db_o)
db_o.close()