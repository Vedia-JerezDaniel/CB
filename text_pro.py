import numpy as np
import pandas as pd
import datetime as dt
import os
from dateutil.relativedelta import *
import re
import pickle
from tqdm.notebook import tqdm

import seaborn as sns; sns.set(style="darkgrid")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams["figure.figsize"] = (18,9)
plt.style.use('fivethirtyeight')

pd.options.display.max_rows = 20
pd.options.display.max_seq_items = 50
pd.set_option('display.max_colwidth', 200)

# Change the name of the excel file to reproduce the other DF

dir_name='E:\\GitRepo\\CB speeches\\data\\'
excel_file = "jpn_pre.xlsx"
read_file = dir_name + excel_file
boe = pd.read_excel(read_file)
boe.shape


def get_split(text, split_len=200, overlap=50):
    '''
    Returns a list of split text of $split_len with overlapping of $overlap.
    Each item of the list will have around split_len length of text.
    '''
    l_total = []
    words = re.findall(r'\b([a-zA-Z]+n\'t|[a-zA-Z]+\'s|[a-zA-Z]+)\b', str(text))    
    if len(words) < split_len:
        n = 1
    else:
        n = (len(words) - overlap) // (split_len - overlap) + 1
        
    for i in range(n):
        l_parcial = words[(split_len - overlap) * i: (split_len - overlap) * i + split_len]
        l_total.append(" ".join(l_parcial))
    return l_total


def get_split_df(df, split_len=200, overlap=50):
    '''
    Returns a dataframe which is an extension of an input dataframe.
    Each row in the new dataframe has less than $split_len words in 'text'.
    '''
    split_data_list = []

    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        #print("Original Word Count: ", row['word_count'])
        text_list = get_split(row["text"], split_len, overlap)
        for text in text_list:
            row['text'] = text
            #print(len(re.findall(r'\b([a-zA-Z]+n\'t|[a-zA-Z]+\'s|[a-zA-Z]+)\b', text)))
            row['wordcount'] = len(re.findall(r'\b([a-zA-Z]+n\'t|[a-zA-Z]+\'s|[a-zA-Z]+)\b', str(text)))
            split_data_list.append(list(row))
            
    split_df = pd.DataFrame(split_data_list, columns=df.columns)
    split_df['RateDecision'] = split_df['RateDecision'].astype('Int8')
    
    return split_df


def remove_short_nokeyword(df, keywords = ['rate', 'rates', 'federal fund', 'outlook', 'forecast', 'employ', 'economy','euro area','balance sheet'], min_times=2):
    '''
    Drop sections which do not have any one of keywords for min_times times
     before applying remove_short_section()
    '''
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
    print("Data Saved to a pickle file in {} !".format(dir_name))
    # Save results to a csv file
    df.to_csv(dir_name + file_name + '.csv', index=True)
    print("Data Saved to a csv file in {} !".format(dir_name))
    

save_data(split_statement_df, "jpn_split")
save_data(keyword_statement_df, "jpn_keyword")