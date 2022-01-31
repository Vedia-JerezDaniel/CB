import pickle
import re
import pandas as pd

# open pickle DF
fu_1 = 'DB/df_fuk'
infile = open(fu_1, 'rb')
df_fu = pickle.load(infile)
kur_1 = 'DB/df_kur1'
infile = open(kur_1, 'rb')
df_kur1 = pickle.load(infile)
kur_2 = 'DB/df_kur2'
infile = open(kur_2, 'rb')
df_kur2 = pickle.load(infile)
kur_3 = 'DB/df_kur3'
infile = open(kur_3, 'rb')
df_kur3 = pickle.load(infile)
kur_4 = 'DB/df_kur4'
infile = open(kur_4, 'rb')
df_kur4 = pickle.load(infile)
kur_20 = 'DB/df_kur20'
infile = open(kur_20, 'rb')
df_kur20 = pickle.load(infile)

shi08 = 'DB/df_shi08'
infile = open(shi08, 'rb')
df_shi08 = pickle.load(infile)
shi_1 = 'DB/df_shi1'
infile = open(shi_1, 'rb')
df_shi1 = pickle.load(infile)
shi_2 = 'DB/df_shi2'
infile = open(shi_2, 'rb')
df_shi2 = pickle.load(infile)

# Merging and cleaning the JAPAN DB
frames = [df_fu, df_shi08,df_kur1, df_kur2, df_kur3, df_kur4, df_shi1, df_shi2, df_kur20]
jpn = pd.concat(frames)
jpn = jpn.sort_index()
jpn['Index'] = range(0, len(jpn))
jpn.drop(["ntex"], inplace=True, axis=1)
jpn['text'] = jpn['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip())
jpn.tail(20)


# saving the pickle
jpn_pk = 'DB/jpn_pickle'
jpn_o = open(jpn_pk, 'wb')
pickle.dump(jpn, jpn_o)
jpn_o.close()
