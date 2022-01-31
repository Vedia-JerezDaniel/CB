import codecs
import datetime as dt
import os
import pickle
import re
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
boe = "DB/boe_pickle"
infile = open(boe, "rb")
boe = pickle.load(infile)

lm = "E:\\GitRepo\\CB speeches\\data\\list_sent"
infile = open(lm, "rb")
lmdict = pickle.load(infile)

neg = "E:\\GitRepo\\CB speeches\\data\\negate"
infile = open(neg, "rb")
negate = pickle.load(infile)

print(len(boe))

## Elapse time
import time
start = time.time()
temp = [tone_count_with_negation_check(lmdict, x) for x in boe.text]
temp = pd.DataFrame(temp)
end = time.time()
print(end - start)

boe["wordcount"] = temp.iloc[:, 0].values
boe["NPositiveWords"] = temp.iloc[:, 1].values
boe["NNegativeWords"] = temp.iloc[:, 2].values

# Sentiment Score normalized by the number of words
boe["sentiment"] = (
    (boe["NPositiveWords"] - boe["NNegativeWords"]) / boe["wordcount"] * 100
)
boe["Poswords"] = temp.iloc[:, 3].values
boe["Negwords"] = temp.iloc[:, 4].values

temp.head()
boe.head()

##
pl = pd.DataFrame()
pl["date"] = pd.to_datetime(boe.index.values, format="%Y-%m-%d")
pl["b"] = pl["date"].apply(lambda x: x.strftime("%Y-%m"))
print(pl["b"])

boe = pd.merge(boe, pl, left_on="Index", right_index=True)
boe.head()
boe.info()
##

import matplotlib.dates as mdates

NetSentiment = boe["NPositiveWords"] - boe["NNegativeWords"]

fig = plt.figure(figsize=(20, 10))
ax = plt.subplot()

plt.plot(boe.date, boe["NPositiveWords"], c="green", linewidth=1.0)
plt.plot(boe.date, boe["NNegativeWords"] * -1, c="red", linewidth=1.0)
plt.plot(boe.date, NetSentiment, c="grey", linewidth=1.0)

plt.title(
    "The number of positive/negative words in statement: Bank of England", fontsize=14
)
plt.legend(
    ["Positive Words", "Negative Words", "Net Sentiment"], prop={"size": 8}, loc=1
)

ax.fill_between(
    boe.date,
    NetSentiment,
    where=(NetSentiment > 0),
    color="green",
    alpha=0.3,
    interpolate=True,
)
ax.fill_between(
    boe.date,
    NetSentiment,
    where=(NetSentiment <= 0),
    color="red",
    alpha=0.3,
    interpolate=True,
)

import matplotlib.dates as mdates

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

datemin = np.datetime64(boe.date[0], "Y")
datemax = np.datetime64(boe.date[-1], "Y") + np.timedelta64(1, "Y")
# plt.xticks(range(len(pl.b)), pl.b, rotation = 'vertical',fontsize=8)
ax.set_xlim(datemin, datemax)
ax.grid(True)
plt.show()
# fig.savefig("boe_1.pdf")
fig.savefig("boe_1.png")

## Net Sentimen analysis
NetSentiment = boe["NPositiveWords"] - boe["NNegativeWords"]

# Normalize data
NPositiveWordsNorm = (
    boe["NPositiveWords"] / boe["wordcount"] * np.mean(boe["wordcount"])
)
NNegativeWordsNorm = (
    boe["NNegativeWords"] / boe["wordcount"] * np.mean(boe["wordcount"])
)
NetSentimentNorm = NPositiveWordsNorm - NNegativeWordsNorm

fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(boe.date, NPositiveWordsNorm, c="green", linewidth=1.0)
plt.plot(boe.date, NNegativeWordsNorm, c="red", linewidth=1.0)

plt.title("Counts normalized by the number of words", fontsize=16)
plt.legend(
    ["Count of Positive Words", "Count of Negative Words"], prop={"size": 12}, loc=1
)

# format the ticks
# round to nearest years.
import matplotlib.dates as mdates

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")
# format the coords message box
datemin = np.datetime64(boe.date[0], "Y")
datemax = np.datetime64(boe.date[-1], "Y") + np.timedelta64(1, "Y")
# plt.xticks(range(0,len(pl.b),6), pl.b, rotation = 45,fontsize=8)
ax.set_xlim(datemin, datemax)
# format the coords message box
ax.format_xdata = mdates.DateFormatter("%Y-%m-%d")
ax.grid(True)
plt.show()
fig.savefig("norm.png")

import nltk.data
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

## Loading interest rates DB
boerate = pd.read_excel(r"DB/int.xlsx")
boerate["Date"] = pd.to_datetime(boerate.Date.values, format="%Y-%m-%d")
boerate.set_index(["Date"])
boerate.fillna(method="ffill", inplace=True)
boerate.info()

selected_columns = boerate[["Date", "Official Rate"]]
rate_df = selected_columns.copy()
rate_df.rename(columns={"Official Rate": "Rate"}, inplace=True)

datetime_series = pd.to_datetime(rate_df["Date"])
datetime_index = pd.DatetimeIndex(datetime_series.values)
rate_df = rate_df.set_index(datetime_index)
print(rate_df.index)

fig, ax = plt.subplots(figsize=(15, 7))
plt.title("Official interest rate: United Kingdom", fontsize=16)
ax.plot(rate_df.Date, rate_df["Rate"].values, c="green", linewidth=1.0)
ax.grid(True)
plt.show()
fig.savefig("rate.png")

## Adding interest rate decision
boe["RateDecision"] = None
boe["Rate"] = None

for i in range(len(boe)):
    for j in range(len(rate_df)):
        if boe.date[i] == rate_df.Date[j]:
            boe["Rate"][i] = float(rate_df["Rate"][j + 1])

boe.head(10)

# checking for NAS, possible due to spare days
boe[boe["Rate"].isna()]
boe["Rate"].fillna(method="ffill", inplace=True)

for i in range(len(boe) - 1):
    if boe["Rate"][i] == boe["Rate"][i + 1]:
        boe["RateDecision"][i] = 0
    elif boe["Rate"][i] < boe["Rate"][i + 1]:
        boe["RateDecision"][i] = 1
    elif boe["Rate"][i] > boe["Rate"][i + 1]:
        boe["RateDecision"][i] = -1

boe.head(10)

boe[boe["RateDecision"].isna()]
boe["Rate"].fillna(method="ffill", inplace=True)

## saving the pickle
rate_des_pickle = "DB/rate_boe"
rate_des_o = open(rate_des_pickle, "wb")
pickle.dump(boe, rate_des_o)
rate_des_o.close()

# to excel
boe.to_excel("E:\\GitRepo\\CB speeches\\data\\sent_BOE.xlsx",
    sheet_name="BOE", engine="xlsxwriter")

# Speaker window
King = np.logical_and(boe.index > "2003-07-01", boe.index < "2013-07-01")
Carney = np.logical_and(boe.index > "2013-07-01", boe.index < "2020-03-15")
Bailey = np.logical_and(boe.index > "2020-03-16", boe.index < "2028-03-16")
Speaker = np.logical_or.reduce((King, Bailey))

# Moving Average
Window = round(0.025 * len(boe))
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
fig, ax = plt.subplots(figsize=(15, 7))
plt.title("Sentiment analysis evolution", fontsize=16)

ax.scatter(boe.date, boe["Rate"] * 15, c="blue", alpha=0.5)
ax.plot(boe.date, CompToMA, c="red", linewidth=2.0)
ax.plot(boe.date, NetSentimentNorm, c="green", linewidth=1, alpha=0.5)
ax.legend(
    [
        str(str(Window) + " statements moving average"),
        "Net sentiment of individual statements",
        "BOE Funds Rate",
    ],
    prop={"size": 12},
    loc=1,
)

import datetime
# Format X-axis
import matplotlib.dates as mdates

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

# Set X-axis and Y-axis range
datemin = np.datetime64(boe.date[0], "Y")
datemax = np.datetime64(boe.date[-1], "Y") + np.timedelta64(1, "Y")
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
    boe.index, 0, 10, where=Speaker, facecolor="lightblue", alpha=0.5, transform=trans
)

# Add text
props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
ax.text(
    0.15,
    0.75,
    "Sir Mervyn King",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)
ax.text(
    0.56,
    0.75,
    "Mark Carney",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)
ax.text(
    0.92,
    0.75,
    "Andrew Bailey",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)

# Add annotations
q1 = mdates.date2num(datetime.datetime(2009, 3, 15))
q2 = mdates.date2num(datetime.datetime(2012, 7, 13))
q3 = mdates.date2num(datetime.datetime(2016, 8, 1))
q4 = mdates.date2num(datetime.datetime(2020, 3, 10))
q41 = mdates.date2num(datetime.datetime(2020, 6, 13))
q42 = mdates.date2num(datetime.datetime(2020, 11, 18))

arrow_style = dict(facecolor="black", edgecolor="white", shrink=0.05)
ax.annotate(
    "QE1",
    xy=(q1, 6),
    xytext=(q1, -8),
    size=10,
    ha="left",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE2",
    xy=(q2, 6),
    xytext=(q2, -8),
    size=10,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE3",
    xy=(q3, 5),
    xytext=(q3, -9),
    size=10,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "Covid-19",
    xy=(q4, 2),
    xytext=(q4, -12),
    size=10,
    ha="right",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "CV+",
    xy=(q41, 3),
    xytext=(q41, -12),
    size=10,
    ha="left",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "CV+2",
    xy=(q42, 3),
    xytext=(q42, -12),
    size=10,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)

plt.show()
fig.savefig("sentiment.png")


## TO QUATERLY
boe.info()
boe.index = pd.to_datetime(boe.index)
b2 = boe.resample("QS").sum()
b2['ind'] = boe.Index.resample("QS").count()
b2.head(10)
b2.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\eda_BOE.xlsx",
    sheet_name="BOE",
    engine="xlsxwriter",
)

## BOE to excel file for topics creation
boe.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\topic_BOE.xlsx",
    sheet_name="BOE",
    engine="xlsxwriter",
)