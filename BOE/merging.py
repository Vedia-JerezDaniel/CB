import pandas as pd
import re
import pickle

# open pickle DF
king08 = 'DB\\df_king08'
infile = open(king08,'rb')
df_king08 = pickle.load(infile)

king = 'DB\\df_king'
infile = open(king,'rb')
df_king = pickle.load(infile)

bailey = 'DB\\df_bailey'
infile = open(bailey,'rb')
df_bailey = pickle.load(infile)

bailey20 = 'DB\\df_bailey20'
infile = open(bailey20,'rb')
df_bailey20 = pickle.load(infile)

car1 = 'DB\\df_car1'
infile = open(car1,'rb')
df_car1 = pickle.load(infile)

car2 = 'DB\\df_car2'
infile = open(car2,'rb')
df_car2 = pickle.load(infile)

car3 = 'DB\\df_car3'
infile = open(car3,'rb')
df_car3 = pickle.load(infile)
infile.close()

## Merging and cleaning the BOE DB
frames = [df_bailey,df_car1,df_car2,df_car3,df_king,df_king08]
boe = pd.concat(frames)

boe.drop(['text'], axis=1, inplace=True)
boe = boe.rename({'ntex': 'text'}, axis=1)
mask = [boe, df_bailey20]
boe = pd.concat(mask)
boe = boe.sort_index()
boe['Index'] = range(0, len(boe))
boe.tail(20)

## saving the pickle
boe_pk = 'DB\\boe_pickle'
boe_o = open(boe_pk,'wb')
pickle.dump(boe, boe_o)
boe_o.close()
