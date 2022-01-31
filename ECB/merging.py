import pandas as pd
import re
import pickle

# open pickle DF
tri08 = 'DB/df_tri08' 
infile = open(tri08,'rb')
df_tri08 = pickle.load(infile)
tri_1 = 'DB/df_tri1' 
infile = open(tri_1,'rb')
df_tri1 = pickle.load(infile)
tri_2 = 'DB/df_tri2' 
infile = open(tri_2,'rb')
df_tri2 = pickle.load(infile)
tri_3 = 'DB/df_tri3' 
infile = open(tri_3,'rb')
df_tri3 = pickle.load(infile)
tri_4 = 'DB/df_tri4' 
infile = open(tri_4,'rb')
df_tri4 = pickle.load(infile)

# DRAGUI MARIO
dra_1 = 'DB/df_dra1' 
infile = open(dra_1,'rb')
df_dra1 = pickle.load(infile)
dra_2 = 'DB/df_dra2' 
infile = open(dra_2,'rb')
df_dra2 = pickle.load(infile)
dra_3 = 'DB/df_dra3' 
infile = open(dra_3,'rb')
df_dra3 = pickle.load(infile)
dra_4 = 'DB/df_dra4' 
infile = open(dra_4,'rb')
df_dra4 = pickle.load(infile)
dra_41 = 'DB/df_dra41' 
infile = open(dra_41,'rb')
df_dra41 = pickle.load(infile)
dra_5 = 'DB/df_dra5' 
infile = open(dra_5,'rb')
df_dra5 = pickle.load(infile)
dra_6 = 'DB/df_dra6' 
infile = open(dra_6,'rb')
df_dra6 = pickle.load(infile)
dra_7 = 'DB/df_dra7' 
infile = open(dra_7,'rb')
df_dra7 = pickle.load(infile)

# LAGARDE CRHISTINE
lag1 = 'DB/df_lag1'
infile = open(lag1,'rb')
df_lag1 = pickle.load(infile)
lag2 = 'DB/df_lag2'
infile = open(lag2,'rb')
df_lag2 = pickle.load(infile)
lag20 = 'DB/df_lag20'
infile = open(lag20,'rb')
df_lag20 = pickle.load(infile)
infile.close()

## Merging and cleaning the ECB DB
frames = [df_tri08,df_tri1,df_tri2,df_tri3,df_tri4,df_dra1,df_dra2,df_dra3,df_dra4,df_dra41,df_dra5,df_dra6,df_dra7,df_lag1, df_lag2, df_lag20]

ecb = pd.concat(frames)
ecb = ecb.sort_index()
ecb['Index'] = range(0, len(ecb))
ecb.drop(['ntex'], axis=1, inplace=True)
ecb.tail(10)

ecb['text'] = ecb['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())

## saving the pickle
ecb_pk = 'DB/ecb_pickle'
ecb_o = open(ecb_pk,'wb')
pickle.dump(ecb, ecb_o)
ecb_o.close()
