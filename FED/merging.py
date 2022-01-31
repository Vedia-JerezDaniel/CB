import pandas as pd
import re
import pickle

# open pickle DF
ber08 = 'DB/df_ber08' 
infile = open(ber08,'rb')
df_ber08 = pickle.load(infile)
ber_1 = 'DB/df_ber1' 
infile = open(ber_1,'rb')
df_ber1 = pickle.load(infile)
ber_2 = 'DB/df_ber2' 
infile = open(ber_2,'rb')
df_ber2 = pickle.load(infile)
ber_3 = 'DB/df_ber3' 
infile = open(ber_3,'rb')
df_ber3 = pickle.load(infile)
ber_4 = 'DB/df_ber4' 
infile = open(ber_4,'rb')
df_ber4 = pickle.load(infile)

yel_1 = 'DB/df_yel1' 
infile = open(yel_1,'rb')
df_yel1 = pickle.load(infile)
yel_2 = 'DB/df_yel2'
infile = open(yel_2,'rb')
df_yel2 = pickle.load(infile)

pow_1 = 'DB/df_pow1' 
infile = open(pow_1,'rb')
df_pow1 = pickle.load(infile)
pow_2 = 'DB/df_pow20' 
infile = open(pow_2,'rb')
df_pow2 = pickle.load(infile)

## Merging and cleaning the FED DB
frames = [df_ber08,df_ber1,df_ber2,df_ber3,df_ber4,df_pow1,df_pow2,df_yel1,df_yel2]
fed = pd.concat(frames)
fed = fed.sort_index()
fed['Index'] = range(0, len(fed))
fed.drop(['ntex'],inplace=True, axis=1)
fed['text'] = fed['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
fed.tail()

## saving the pickle
fed_pk = 'DB/fed_pickle'
fed_o = open(fed_pk,'wb')
pickle.dump(fed, fed_o)
fed_o.close()


