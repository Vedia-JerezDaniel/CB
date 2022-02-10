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

ecb_c = "DB/rate_ecb"
infile = open(ecb_c, "rb")
ecb = pickle.load(infile)

ecb.rename(index={"2010-16-15": "2010-12-15"}, inplace=True)
ecb["ntex"] = ecb["text"].apply(
    lambda x: x.replace("\n", " ").replace("\r", " ").strip()
)
ecb.tail(50)

lm = "E:\\GitRepo\\CB speeches\\data\\list_sent"
infile = open(lm, "rb")
lmdict = pickle.load(infile)

neg = "E:\\GitRepo\\CB speeches\\data\\negate"
infile = open(neg, "rb")
negate = pickle.load(infile)

print(len(ecb))

## Elapse time
import time
start = time.time()
temp = [tone_count_with_negation_check(lmdict, x) for x in ecb.text]
temp = pd.DataFrame(temp)
end = time.time()
print(end - start)

ecb["wordcount"] = temp.iloc[:, 0].values
ecb["NPositiveWords"] = temp.iloc[:, 1].values
ecb["NNegativeWords"] = temp.iloc[:, 2].values

# Sentiment Score normalized by the number of words
ecb["sentiment"] = (
    (ecb["NPositiveWords"] - ecb["NNegativeWords"]) / ecb["wordcount"] * 100
)
ecb["Poswords"] = temp.iloc[:, 3].values
ecb["Negwords"] = temp.iloc[:, 4].values

temp.head()
ecb.head()

##
pl = pd.DataFrame()
pl["date"] = pd.to_datetime(ecb.index.values, format="%Y-%m-%d")
pl["b"] = pl["date"].apply(lambda x: x.strftime("%Y-%m"))
print(pl["b"])

ecb = pd.merge(ecb, pl, left_on="Index", right_index=True)
ecb.head()
ecb.info()

## Net Sentimen analysis
import matplotlib.dates as mdates
NetSentiment = ecb["NPositiveWords"] - ecb["NNegativeWords"]

fig = plt.figure(figsize=(20, 10))
ax = plt.subplot()

plt.plot(ecb.date, ecb["NPositiveWords"], c="green", linewidth=1.0)
plt.plot(ecb.date, ecb["NNegativeWords"] * -1, c="red", linewidth=1.0)
plt.plot(ecb.date, NetSentiment, c="grey", linewidth=1.0)

plt.title(
    "The number of positive/negative words in statement: European Central Bank",
    fontsize=14,
)
plt.legend(
    ["Positive Words", "Negative Words", "Net Sentiment"], prop={"size": 8}, loc=1
)

ax.fill_between(
    ecb.date,
    NetSentiment,
    where=(NetSentiment > 0),
    color="green",
    alpha=0.3,
    interpolate=True,
)
ax.fill_between(
    ecb.date,
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

datemin = np.datetime64(ecb.date[0], "Y")
datemax = np.datetime64(ecb.date[-1], "Y") + np.timedelta64(1, "Y")
# plt.xticks(range(len(pl.b)), pl.b, rotation = 'vertical',fontsize=8)
ax.set_xlim(datemin, datemax)
ax.grid(True)
plt.show()
fig.savefig("num.png")

# Normalize data
NPositiveWordsNorm = (
    ecb["NPositiveWords"] / ecb["wordcount"] * np.mean(ecb["wordcount"])
)
NNegativeWordsNorm = (
    ecb["NNegativeWords"] / ecb["wordcount"] * np.mean(ecb["wordcount"])
)
NetSentimentNorm = NPositiveWordsNorm - NNegativeWordsNorm

fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(ecb.date, NPositiveWordsNorm, c="green", linewidth=1.0)
plt.plot(ecb.date, NNegativeWordsNorm, c="red", linewidth=1.0)
plt.title("Counts normalized by the number of words", fontsize=16)
plt.legend(
    ["Count of Positive Words", "Count of Negative Words"], prop={"size": 12}, loc=1
)

# format the ticks
# round to nearest years.
years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")

# format the coords message box
datemin = np.datetime64(ecb.date[0], "Y")
datemax = np.datetime64(ecb.date[-1], "Y") + np.timedelta64(1, "Y")
# plt.xticks(range(0,len(pl.b),6), pl.b, rotation = 45,fontsize=8)
ax.set_xlim(datemin, datemax)
# format the coords message box
ax.format_xdata = mdates.DateFormatter("%Y-%m-%d")
ax.grid(True)
plt.show()
fig.savefig("norm.png")


## Loading interest rates DB
ecbrate = pd.read_excel(r"DB/int.xlsx")
ecbrate["Date"] = pd.to_datetime(ecbrate.date.values, format="%Y-%m-%d")
ecbrate.set_index(["Date"])
ecbrate.fillna(method="ffill", inplace=True)
ecbrate.info()

selected_columns = ecbrate[["Date", "ECB lending rate"]]
rate_df = selected_columns.copy()
rate_df.rename(columns={"ECB lending rate": "Rate"}, inplace=True)

datetime_series = pd.to_datetime(rate_df["Date"])
datetime_index = pd.DatetimeIndex(datetime_series.values)
rate_df = rate_df.set_index(datetime_index)
print(rate_df.index)

fig, ax = plt.subplots(figsize=(15, 7))
plt.title("Official interest rate: Euro Area", fontsize=16)
ax.plot(rate_df.Date, rate_df["Rate"].values, c="green", linewidth=1.0)
ax.grid(True)
plt.show()
fig.savefig("rate.png")

## Adding interest rate decision
ecb["RateDecision"] = None
ecb["Rate"] = None

for i in range(len(ecb)):
    for j in range(len(rate_df)):
        if ecb.date[i] == rate_df.Date[j]:
            ecb["Rate"][i] = float(rate_df["Rate"][j + 1])

ecb.head(10)

# checking for NAS, possible due to spare days
ecb[ecb["RateDecision"].isna()]
ecb['RateDecision'].fillna(method='ffill', inplace=True)

for i in range(len(ecb) - 1):
    if ecb["Rate"][i] == ecb["Rate"][i + 1]:
        ecb["RateDecision"][i] = 0
    elif ecb["Rate"][i] < ecb["Rate"][i + 1]:
        ecb["RateDecision"][i] = 1
    elif ecb["Rate"][i] > ecb["Rate"][i + 1]:
        ecb["RateDecision"][i] = -1

ecb.head(12)

## saving the pickle
rate_des_pickle = "DB/rate_ecb"
rate_des_o = open(rate_des_pickle, "wb")
pickle.dump(ecb, rate_des_o)
rate_des_o.close()

# to excel
ecb.to_excel("E:\\GitRepo\\CB speeches\\data\\sent_ECB.xlsx", engine="xlsxwriter")

# Speaker window
Trichet = np.logical_and(ecb.index > "2003-11-01", ecb.index < "2011-10-31")
Dragui = np.logical_and(ecb.index > "2011-11-01", ecb.index < "2019-10-31")
Lagarde = np.logical_and(ecb.index > "2019-11-01", ecb.index < "2027-10-31")
Speaker = np.logical_or.reduce((Trichet, Lagarde))

# Moving Average
Window = round(0.025 * len(ecb))
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

ax.scatter(ecb.date, ecb["Rate"] * 15, c="blue", alpha=0.5)
ax.plot(ecb.date, CompToMA, c="red", linewidth=2.0)
ax.plot(ecb.date, NetSentimentNorm, c="green", linewidth=1, alpha=0.5)
ax.legend(
    [
        "ECB Funds Rate", str(str(Window) + " statements moving average"),
        "Net sentiment of individual statements"
            ],
    prop={"size": 14},
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
datemin = np.datetime64(ecb.date[0], "Y")
datemax = np.datetime64(ecb.date[-1], "Y") + np.timedelta64(1, "Y")
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
    ecb.index, 0, 10, where=Speaker, facecolor="lightblue", alpha=0.5, transform=trans
)

# Add text
props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
ax.text(
    0.09,
    0.65,
    "Jean-Claude Trichet",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)
ax.text(
    0.52,
    0.75,
    "Mario Draghi",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)
ax.text(
    0.83,
    0.75,
    "Christine Lagarde",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
)

# Add annotations
cb = mdates.date2num(datetime.datetime(2009, 5, 15))
q1 = mdates.date2num(datetime.datetime(2015, 3, 13))
q11 = mdates.date2num(datetime.datetime(2016, 4, 1))
q2 = mdates.date2num(datetime.datetime(2017, 4, 10))
q21 = mdates.date2num(datetime.datetime(2018, 1, 13))
q22 = mdates.date2num(datetime.datetime(2018, 10, 18))
q3 = mdates.date2num(datetime.datetime(2019, 9, 18))
q31 = mdates.date2num(datetime.datetime(2020, 3, 18))

arrow_style = dict(facecolor="black", edgecolor="white", shrink=0.05)
ax.annotate(
    "CB",
    xy=(cb, 25),
    xytext=(cb, 12),
    size=11,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE1",
    xy=(q1, 2),
    xytext=(q1, -10),
    size=11,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE1+",
    xy=(q11, 2),
    xytext=(q11, -10),
    size=11,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE2",
    xy=(q2, 2),
    xytext=(q2, -10),
    size=11,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE2+",
    xy=(q21, 2),
    xytext=(q21, -11),
    size=11,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE2+",
    xy=(q22, 2),
    xytext=(q22, -14),
    size=11,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE3",
    xy=(q3, 2),
    xytext=(q3, -11),
    size=11,
    ha="right",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)
ax.annotate(
    "QE3+",
    xy=(q31, 2),
    xytext=(q31, -14),
    size=11,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),
)

plt.show()
fig.savefig("sentiment.png")

## TO QUATERLY
ecb.info()
ecb.index = pd.to_datetime(ecb.index)
b2 = ecb.resample("QS").sum()
b2['ind'] = ecb.Index.resample("QS").count()
b2.head(10)
b2.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\eda_ECB.xlsx",
    sheet_name="ECB",
    engine="xlsxwriter",
)

## ECB to excel for topics creation
ecb.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\topic_ECB.xlsx",
    sheet_name="ECB",
    engine="xlsxwriter",
)