import codecs
import datetime as dt
import pickle
import matplotlib.pyplot as plt
#For tokenizing sentences
import nltk
import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm
from tone_count import *

nltk.download('punkt')
plt.style.use('seaborn-whitegrid')

jpn = 'DB/rate_jpn'
infile = open(jpn,'rb')
jpn = pickle.load(infile)
jpn.rename(index={'2009-15-29':'2009-12-29'},inplace=True)
jpn.head(15)

lm = 'E:\\GitRepo\\CB speeches\\data\\list_sent'
infile = open(lm,'rb')
lmdict = pickle.load(infile)

neg = 'E:\\GitRepo\\CB speeches\\data\\negate'
infile = open(neg,'rb')
negate = pickle.load(infile)

print(len(jpn))

## Elapse time
import time
start = time.time()
temp = [tone_count_with_negation_check(lmdict,x) for x in jpn.text]
temp = pd.DataFrame(temp)
end = time.time()
print(end - start)

jpn['wordcount'] = temp.iloc[:,0].values
jpn['NPositiveWords'] = temp.iloc[:,1].values
jpn['NNegativeWords'] = temp.iloc[:,2].values
#Sentiment Score normalized by the number of words
jpn['sentiment'] = (jpn['NPositiveWords'] - jpn['NNegativeWords']) / jpn['wordcount'] * 100
jpn['Poswords'] = temp.iloc[:,3].values
jpn['Negwords'] = temp.iloc[:,4].values

temp.head()
jpn.head()

pl = pd.DataFrame()
pl['date'] = pd.to_datetime(jpn.index.values,format='%Y-%m-%d')
pl["b"] = pl['date'].apply(lambda x: x.strftime('%Y-%m'))
print(pl["b"])

jpn = pd.merge(jpn, pl, left_on='Index', right_index=True)
jpn.head()
jpn.info()
##
## Net Sentimen analysis
import matplotlib.dates as mdates
NetSentiment = jpn['NPositiveWords'] - jpn['NNegativeWords']

fig = plt.figure(figsize=(20,10))
ax = plt.subplot()
plt.plot(jpn.date, jpn['NPositiveWords'], c='green', linewidth= 1.0)
plt.plot(jpn.date, jpn['NNegativeWords']*-1, c='red', linewidth=1.0)
plt.plot(jpn.date, NetSentiment, c='grey', linewidth=1.0)
plt.title('The number of positive/negative words in statement: European Central Bank', fontsize=14)
plt.legend(['Positive Words', 'Negative Words', 'Net Sentiment'], prop={'size': 8}, loc=1)

ax.fill_between(jpn.date, NetSentiment, where=(NetSentiment > 0), color='green', alpha=0.3, interpolate=True)
ax.fill_between(jpn.date, NetSentiment, where=(NetSentiment <= 0), color='red', alpha=0.3, interpolate=True)

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator() # every month
years_fmt = mdates.DateFormatter('%Y')
# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
# Minor ticks every month.
fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

datemin = np.datetime64(jpn.date[0], 'Y')
datemax = np.datetime64(jpn.date[-1], 'Y') + np.timedelta64(1, 'Y')
# plt.xticks(range(len(pl.b)), pl.b, rotation = 'vertical',fontsize=8)
ax.set_xlim(datemin, datemax)
ax.grid(True)
plt.show()
fig.savefig('E:\\GitRepo\\CB speeches\\JPN\\num.png')

# Normalize data
NPositiveWordsNorm = jpn['NPositiveWords'] / jpn['wordcount'] * np.mean(jpn['wordcount'])
NNegativeWordsNorm = jpn['NNegativeWords'] / jpn['wordcount'] * np.mean(jpn['wordcount'])
NetSentimentNorm = (NPositiveWordsNorm - NNegativeWordsNorm)

fig, ax = plt.subplots(figsize=(15,7))
ax.plot(jpn.date, NPositiveWordsNorm, c='green', linewidth= 1.0)
plt.plot(jpn.date, NNegativeWordsNorm, c='red', linewidth=1.0)
plt.title('Counts normalized by the number of words', fontsize=16)
plt.legend(['Count of Positive Words', 'Count of Negative Words'],
           prop={'size': 12},  loc = 1)

# format the ticks round to nearest years.
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')
# format the coords message box
# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
# Minor ticks every month.
fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

datemin = np.datetime64(jpn.date[0], 'Y')
datemax = np.datetime64(jpn.date[-1], 'Y') + np.timedelta64(1, 'Y')
# plt.xticks(range(0,len(pl.b),6), pl.b, rotation = 45,fontsize=8)
ax.set_xlim(datemin, datemax)
# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.grid(True)
plt.show()
fig.savefig('E:\\GitRepo\\CB speeches\\JPN\\norm.png')

## Loading interest rates DB
jpnrate = pd.read_excel(r'DB/rate.xlsx')
# jpnrate['Date'] = pd.to_datetime(jpnrate.date.values,format='%Y-%m-%d')
jpnrate.set_index(['date'])
jpnrate.fillna(method='ffill', inplace=True)
jpnrate.info()

selected_columns = jpnrate[["date","rate"]]
rate_df = selected_columns.copy()
rate_df.rename(columns={"rate": "Rate"}, inplace=True)

datetime_series = pd.to_datetime(rate_df['date'])
datetime_index = pd.DatetimeIndex(datetime_series.values)
rate_df = rate_df.set_index(datetime_index)
print(rate_df.index)

fig, ax = plt.subplots(figsize=(15,7))
plt.title('Official interest rate: Japan', fontsize=16)
ax.plot(rate_df.date, rate_df['Rate'].values, c = 'green', linewidth= 1.0)

# format the ticks round to nearest years.
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')
# format the coords message box
# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
# Minor ticks every month.
fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

datemin = np.datetime64(jpn.date[0], 'Y')
datemax = np.datetime64(jpn.date[-1], 'Y') + np.timedelta64(1, 'Y')
# plt.xticks(range(0,len(pl.b),6), pl.b, rotation = 45,fontsize=8)
ax.set_xlim(datemin, datemax)
# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

ax.grid(True)
plt.show()
fig.savefig('E:\\GitRepo\\CB speeches\\JPN\\rate.png')

rt = rate_df['Rate'].resample('D').ffill()
rt= rt.to_frame()
## Adding interest rate decision
jpn['RateDecision'] = None
jpn['Rate'] = None

for i in range(len(jpn)):
    for j in range(len(rt)):
        if jpn.date[i] == rt.index.values[j]:
            jpn['Rate'][i] = float(rt['Rate'][j+1])

jpn.tail(15)

# #checking for NAS, possible due to spare days
jpn[jpn['Rate'].isna()]
jpn['Rate'].fillna(method='bfill', inplace=True)

for i in range(len(jpn)-1):
    if jpn['Rate'][i] == jpn['Rate'][i+1]:
        jpn['RateDecision'][i] = 0
    elif jpn['Rate'][i] < jpn['Rate'][i+1]:
        jpn['RateDecision'][i] = 1
    elif jpn['Rate'][i] > jpn['Rate'][i+1]:
        jpn['RateDecision'][i] = -1

jpn[jpn['RateDecision'].isna()]
jpn['RateDecision'].fillna(method='ffill', inplace=True)
jpn.tail(15)

## saving the pickle
jpn_pickle = 'DB/jpn_f'
jpn_fo = open(jpn_pickle,'wb')
pickle.dump(jpn, jpn_fo)
jpn_fo.close()

jpn.to_excel("E:\\GitRepo\\CB speeches\\data\\sent_jpn.xlsx", engine='xlsxwriter')

rate_des_pickle = 'DB/rate_jpn'
rate_des_o = open(rate_des_pickle,'wb')
pickle.dump(jpn, rate_des_o)
rate_des_o.close()

#Speaker window
Fukui = np.logical_and(jpn.index > '2003-03-20', jpn.index < '2008-03-19')
Shirakawa = np.logical_and(jpn.index > '2008-04-09', jpn.index < '2013-03-19')
Kuroda = np.logical_and(jpn.index > '2013-03-20', jpn.index < '2023-04-08')
Speaker = np.logical_or.reduce((Fukui, Kuroda))

# Moving Average
Window = round(0.025 * len(jpn))
CompToMA = NetSentimentNorm.rolling(Window).mean()

cmin, cmax = None, None
if CompToMA.min() < NetSentimentNorm.min():
    cmin = CompToMA.min()
else:
    cmin = NetSentimentNorm.min()
if CompToMA.max() > NetSentimentNorm.max():
    cmax = CompToMA.max()
else:
    cmax = NetSentimentNorm.max()

# Final Plotting Data
fig, ax = plt.subplots(figsize=(15,7))
plt.title('Sentiment analysis evolution', fontsize=16)
ax.scatter(jpn.date, jpn['Rate']*180, c = 'blue', alpha = 0.5)
ax.plot(jpn.date, CompToMA, c = 'red', linewidth= 2.0)
ax.plot(jpn.date, NetSentimentNorm,  c = 'green', linewidth= 1, alpha = 0.5)
ax.legend(['Japan Rate', str(str(Window) + ' statements moving average'),
           'Net sentiment of individual statements'], prop={'size': 14}, loc = 1)

import datetime
# Format X-axis
import matplotlib.dates as mdates

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

# Set X-axis and Y-axis range
datemin = np.datetime64(jpn.date[0], 'Y')
datemax = np.datetime64(jpn.date[-1], 'Y') + np.timedelta64(1, 'Y')
ax.set_xlim(datemin, datemax)
# plt.xticks(range(0,len(pl.b),6), pl.b, rotation = 45,fontsize=8)
ax.set_ylim(cmin+5,cmax+5)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.grid(True)
ax.tick_params(axis='both', which='major', labelsize=12)

# Fill speaker
import matplotlib.transforms as mtransforms

trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
theta = 0.9
ax.fill_between(jpn.index, 0, 10, where = Speaker, facecolor='lightblue', alpha=0.5, transform=trans)

# Add text
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.005, 0.73, "Toshihiko Fukui", transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax.text(0.20, 0.75, "Masaaki Shirakawa", transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)
ax.text(0.63, 0.75, "Haruhiko Kuroda", transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)

# Add annotations
qe_0 = (mdates.date2num(datetime.datetime(2011,8,13)))
qe = (mdates.date2num(datetime.datetime(2013,4,13)))
qe1 = (mdates.date2num(datetime.datetime(2014,10,1)))
qe2 = (mdates.date2num(datetime.datetime(2016,7,29)))
qe3 = (mdates.date2num(datetime.datetime(2018,7,31)))
cov = (mdates.date2num(datetime.datetime(2020,3,16)))
cov1 = (mdates.date2num(datetime.datetime(2020,4,27)))

arrow_style = dict(facecolor='black', edgecolor='white', shrink=0.05)
ax.annotate('QE', xy=(qe_0, 50), xytext=(qe_0, 30), size=11, ha='center', verticalalignment= 'bottom',
arrowprops=dict(arrow_style, shrink=0.05,ls='--', color='gray',lw=0.5))
ax.annotate('QE1', xy=(qe, 50), xytext=(qe, 30), size=11, ha='center', verticalalignment= 'bottom',
arrowprops=dict(arrow_style, shrink=0.05,ls='--', color='gray',lw=0.5))
ax.annotate('QE1+', xy=(qe1, 50), xytext=(qe1, 30), size=11, ha='center', verticalalignment= 'bottom',
arrowprops=dict(arrow_style, shrink=0.05,ls='--', color='gray',lw=0.5))
ax.annotate('QE2', xy=(qe2, 50), xytext=(qe2, 30), size=11, ha='center', verticalalignment= 'bottom',
arrowprops=dict(arrow_style, shrink=0.05,ls='--', color='gray',lw=0.5))
ax.annotate('QE3', xy=(qe3, 40), xytext=(qe3, 25), size=11, ha='center', verticalalignment= 'bottom',
arrowprops=dict(arrow_style, shrink=0.05,ls='--', color='gray',lw=0.5))
ax.annotate('Cov-19', xy=(cov,20), xytext=(cov, 10), size=11, ha='right', verticalalignment= 'bottom',
arrowprops=dict(arrow_style, shrink=0.05,ls='--', color='gray',lw=0.5))
ax.annotate('Cov-19+', xy=(cov1, 20), xytext=(cov1, 10), size=11, ha='left', verticalalignment= 'bottom',
arrowprops=dict(arrow_style, shrink=0.05,ls='--', color='gray',lw=0.5))
plt.show()

fig.savefig('E:\\GitRepo\\CB speeches\\JPN\\sentiment.png')

## TO QUATERLY
jpn.info()
jpn.index = pd.to_datetime(jpn.index)
b2 = jpn.resample('QS').sum()
b2['ind']=jpn.Index.resample('QS').count()
b2.head(10)
b2.to_excel("E:\\GitRepo\\CB speeches\\data\\eda_JPN.xlsx", sheet_name='JPN',engine='xlsxwriter')

## JPN for topic creation
jpn.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\Topic_JPN.xlsx",
    sheet_name="JPN",
    engine="xlsxwriter",
)