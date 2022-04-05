import numpy as np
import pandas as pd
from dateutil.relativedelta import *
import pickle
import seaborn as sns; sns.set(style="darkgrid")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from getsplit import *
import os

plt.rcParams["figure.figsize"] = (18,9)
plt.style.use('fivethirtyeight')

pd.options.display.max_rows = 20
pd.options.display.max_seq_items = 50
pd.set_option('display.max_colwidth', 200)

# Change the name of the excel file to reproduce the other DF

dir_name='E:\\GitRepo\\CB speeches\\data\\'
excel_file = "jpn_pre.xlsx"
read_file = dir_name + excel_file
boe = pd.read_excel("read_file")
# boe = pd.read_excel("/home/dani/Escritorio/Gitrepo/CB/data/boe_pre.xlsx")
boe.shape


def remove_short_nokeyword(df, keywords = None, min_times=2):
    '''
    Drop sections which do not have any one of keywords for min_times times
     before applying remove_short_section()
    '''
    if keywords is None:
        keywords = ['rate', 'rates', 'federal fund', 'outlook', 'forecast', 'employ', 'economy', 'euro area', 'balance sheet']

    new_df = df.copy()
    new_section_list = []
    ne=[]
    # for _, row in tqdm(new_df.iterrows(), total=new_df.shape[0]):
    #     new_section = [sec for sec in row['text'] if len(set(sec.split()).intersection(keywords)) > min_times]
    #     new_section_list.append(new_section)
    for j in boe['text']:
        if len(set(str(j).split()).intersection(keywords)) > min_times:
            ne=j
        new_section_list.append(ne)

    new_df['text'] = new_section_list
    return new_df


# Missing rate changed
boe.loc[boe['Rate'].isnull()]
boe["Rate"].fillna(method="bfill", inplace=True)

# Plotting word_count
plt.figure(figsize=(10,5))
sns.distplot(boe["wordcount"].values, bins=50)
plt.show()

### Split contents to max 200 words
split_statement_df = get_split_df(boe)
split_statement_df.tail(10)

# Keep sections having keywords and long enough
keyword_statement_df = remove_short_nokeyword(boe)
keyword_statement_df.reset_index(drop=True, inplace=True)
print(keyword_statement_df.shape)
keyword_statement_df.head(9)


def save_data(df, file_name, dir_name='../data/preprocessed/'):
    '''
    Save the given df to pickle file and csv file in the given directory.
    '''
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    with open(dir_name + file_name + '.pickle', 'wb') as file:
        pickle.dump(df, file)
    print(f"Data Saved to a pickle file in {dir_name} !")
    # Save results to a csv file
    df.to_csv(dir_name + file_name + '.csv', index=True)
    print(f"Data Saved to a csv file in {dir_name} !")
    

save_data(split_statement_df, "jpn_split")
save_data(keyword_statement_df, "jpn_keyword")