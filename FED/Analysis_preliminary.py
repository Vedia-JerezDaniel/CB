import codecs
import datetime as dt
import pickle
import matplotlib.pyplot as plt

# For tokenizing sentences
import nltk
import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm
from tone_count import *

nltk.download("punkt")
plt.style.use("seaborn-whitegrid")

# open list pickle
fed = "DB/fed_pickle"
infile = open(fed, "rb")
fed = pickle.load(infile)

lm = "E:\\GitRepo\\CB speeches\\data\\list_sent"
infile = open(lm, "rb")
lmdict = pickle.load(infile)

neg = "E:\\GitRepo\\CB speeches\\data\\negate"
infile = open(neg, "rb")
negate = pickle.load(infile)

print(len(fed))

## Elapse time
import time

start = time.time()
temp = [tone_count_with_negation_check(lmdict, x) for x in fed.text]
temp = pd.DataFrame(temp)
end = time.time()
print(end - start)

fed["wordcount"] = temp.iloc[:, 0].values
fed["NPositiveWords"] = temp.iloc[:, 1].values
fed["NNegativeWords"] = temp.iloc[:, 2].values
# Sentiment Score normalized by the number of words
fed["sentiment"] = (
    (fed["NPositiveWords"] - fed["NNegativeWords"]) / fed["wordcount"] * 100
)
fed["Poswords"] = temp.iloc[:, 3].values
fed["Negwords"] = temp.iloc[:, 4].values

temp.head()
fed.head()

##
pl = pd.DataFrame()
pl["date"] = pd.to_datetime(fed.index.values, format="%Y-%m-%d")
pl["b"] = pl["date"].apply(lambda x: x.strftime("%Y-%m"))
print(pl["b"])

fed = pd.merge(fed, pl, left_on="Index", right_index=True)
fed.head()
fed.info()
##

## Net Sentimen analysis
import matplotlib.dates as mdates
NetSentiment = fed["NPositiveWords"] - fed["NNegativeWords"]

fig = plt.figure(figsize=(20, 10))
ax = plt.subplot()
plt.plot(fed.date, fed["NPositiveWords"], c="green", linewidth=1.0)
plt.plot(fed.date, fed["NNegativeWords"] * -1, c="red", linewidth=1.0)
plt.plot(fed.date, NetSentiment, c="grey", linewidth=1.0)

plt.title(
    "The number of positive/negative words in statement: Federal Reserve", fontsize=14
)
plt.legend(
    ["Positive Words", "Negative Words", "Net Sentiment"], prop={"size": 8}, loc=1
)

ax.fill_between(
    fed.date,
    NetSentiment,
    where=(NetSentiment > 0),
    color="green",
    alpha=0.3,
    interpolate=True,
)
ax.fill_between(
    fed.date,
    NetSentiment,
    where=(NetSentiment <= 0),
    color="red",
    alpha=0.3,
    interpolate=True,
)

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")
# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
# Minor ticks every month.
fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

datemin = np.datetime64(fed.date[0], "Y")
datemax = np.datetime64(fed.date[-1], "Y") + np.timedelta64(1, "Y")
# plt.xticks(range(len(pl.b)), pl.b, rotation = 'vertical',fontsize=8)
ax.set_xlim(datemin, datemax)
ax.grid(True)
plt.show()
fig.savefig("num.png")

# Normalize data
NPositiveWordsNorm = (
    fed["NPositiveWords"] / fed["wordcount"] * np.mean(fed["wordcount"])
)
NNegativeWordsNorm = (
    fed["NNegativeWords"] / fed["wordcount"] * np.mean(fed["wordcount"])
)
NetSentimentNorm = NPositiveWordsNorm - NNegativeWordsNorm

fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(fed.date, NPositiveWordsNorm, c="green", linewidth=1.0)
plt.plot(fed.date, NNegativeWordsNorm, c="red", linewidth=1.0)
plt.title("Counts normalized by the number of words", fontsize=16)
plt.legend(
    ["Count of Positive Words", "Count of Negative Words"], prop={"size": 12}, loc=1
)

# format the ticks round to nearest years.
years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")
# format the coords message box
datemin = np.datetime64(fed.date[0], "Y")
datemax = np.datetime64(fed.date[-1], "Y") + np.timedelta64(1, "Y")
# plt.xticks(range(0,len(pl.b),6), pl.b, rotation = 45,fontsize=8)
ax.set_xlim(datemin, datemax)
# format the coords message box
ax.format_xdata = mdates.DateFormatter("%Y-%m-%d")
ax.grid(True)
plt.show()
fig.savefig("norm.png")

## Loading interest rates DB
fedrate = pd.read_excel(r"DB/int.xlsx")
fedrate["Date"] = pd.to_datetime(fedrate.date.values, format="%Y-%m-%d")
fedrate.set_index(["Date"])
fedrate.fillna(method="ffill", inplace=True)
fedrate.info()

selected_columns = fedrate[["Date", "EFFR"]]
rate_df = selected_columns.copy()
rate_df.rename(columns={"EFFR": "Rate"}, inplace=True)

datetime_series = pd.to_datetime(rate_df["Date"])
datetime_index = pd.DatetimeIndex(datetime_series.values)
rate_df = rate_df.set_index(datetime_index)
print(rate_df.index)

fig, ax = plt.subplots(figsize=(15, 7))
plt.title("Official interest rate: FED", fontsize=16)
ax.plot(rate_df.Date, rate_df["Rate"].values, c="green", linewidth=1.0)
ax.grid(True)
plt.show()
fig.savefig("rate.png")

## Adding interest rate decision
fed["RateDecision"] = None
fed["Rate"] = None

for i in range(len(fed)):
    for j in range(len(rate_df)):
        if fed.date[i] == rate_df.Date[j]:
            fed["Rate"][i] = float(rate_df["Rate"][j + 1])
fed.head(10)

# checking for NAS, possible due to spare days
fed[fed["Rate"].isna()]
fed["Rate"].fillna(method="ffill", inplace=True)

for i in range(len(fed) - 1):
    if fed["Rate"][i] == fed["Rate"][i + 1]:
        fed["RateDecision"][i] = 0
    elif fed["Rate"][i] < fed["Rate"][i + 1]:
        fed["RateDecision"][i] = 1
    elif fed["Rate"][i] > fed["Rate"][i + 1]:
        fed["RateDecision"][i] = -1

fed.head(10)

## saving the pickle
rate_des_pickle = "DB/rate_fed"
rate_des_o = open(rate_des_pickle, "wb")
pickle.dump(fed, rate_des_o)
rate_des_o.close()

# to excel
fed.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\sent_ex.xlsx",
    sheet_name="FED",
    engine="xlsxwriter",
)

# Speaker window
Bernanke = np.logical_and(fed.index > "2006-2-01", fed.index < "2014-1-31")
Yellen = np.logical_and(fed.index > "2014-2-03", fed.index < "2018-2-03")
Powell = np.logical_and(fed.index > "2018-2-05", fed.index < "2022-2-05")
Speaker = np.logical_or.reduce((Bernanke, Powell))

# Moving Average
Window = int(np.round(len(fed) * 0.03))
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

# Plotting Data
import datetime
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(15, 7))
plt.title("Sentiment analysis evolution", fontsize=16)

ax.plot(fed.date, CompToMA, c="red", linewidth=2.0)
ax.plot(fed.date, NetSentimentNorm, c="green", linewidth=1, alpha=0.5)
ax.legend(
    [
        str(str(Window) + " statements moving average"),
        "Net sentiment of individual statements",
        "FED Funds Rate",
    ],
    prop={"size": 14},
    loc=2,
)

# ax2 = ax1.twinx()
ax.scatter(fed.date, fed["Rate"] * 30, c="blue", alpha=0.5)
# ax2.set_ylabel('FER Rate')

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
# Set X-axis and Y-axis range
datemin = np.datetime64(fed.date[0], "Y")
datemax = np.datetime64(fed.date[-1], "Y") + np.timedelta64(1, "Y")
ax.set_xlim(datemin, datemax)
# plt.xticks(range(0,len(pl.b),6), pl.b, rotation = 45,fontsize=8)
ax.set_ylim(cmin + 5, cmax + 5)

# format the coords message box
ax.format_xdata = mdates.DateFormatter("%Y-%m-%d")
ax.grid(True)
ax.tick_params(axis="both", which="major", labelsize=12)

# Fill speaker
import matplotlib.transforms as mtransforms

trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
theta = 0.9
ax.fill_between(
    fed.index, 0, 10, where=Speaker, facecolor="lightblue", alpha=0.5, transform=trans
)

# Add text
props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
ax.text(
    0.19,
    0.75,
    "Ben Bernanke",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)
ax.text(
    0.72,
    0.75,
    "Janet Yellen",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)
ax.text(
    0.93,
    0.75,
    "Jay Powell",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)

# Add annotations
q1 = mdates.date2num(datetime.datetime(2008, 12, 1))
q2 = mdates.date2num(datetime.datetime(2010, 11, 3))
twist = mdates.date2num(datetime.datetime(2011, 9, 21))
q3 = mdates.date2num(datetime.datetime(2013, 9, 13))
covid = mdates.date2num(datetime.datetime(2020, 3, 18))

arrow_style = dict(facecolor="black", edgecolor="white", shrink=0.05)
ax.annotate(
    "QE1",
    xy=(q1, 0),
    xytext=(q1, -24),
    size=12,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE2",
    xy=(q2, 0),
    xytext=(q2, -24),
    size=12,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "Twist",
    xy=(twist, 0),
    xytext=(twist, -24),
    size=12,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE3",
    xy=(q3, 0),
    xytext=(q3, -24),
    size=12,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "Covid-19",
    xy=(covid, 0),
    xytext=(covid, -24),
    size=12,
    ha="left",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
plt.show()
fig.savefig("sentim.png")

## TO QUATERLY
fed.info()
fed.index = pd.to_datetime(fed.index)
b2 = fed.resample("QS").sum()
b2['ind'] = fed.Index.resample("QS").count()
b2.head(10)
b2.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\eda_FED.xlsx",
    sheet_name="FED",
    engine="xlsxwriter",
)

## FEd file for topic creation
fed.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\topic_FED.xlsx",
    sheet_name="FED",
    engine="xlsxwriter",
)