

This page contains the Python code for my Medium blog publication entitled: ā[Sentiment Analysis of Monetary Policy Communication: Part Iā](https://danielvediajerez.medium.com/sentiment-analysis-of-central-bank-monetary-policy-communication-e6bca0a7cb7b). Visit the site for the analysis and to see its following part on Covid-19 and Monetary Policy sentiments in the Euro Area.

Here, we add all the Python code for making the analysis, measure the Sentiment index for the Monetary Policy for the four main central banks of the world: Federal Reserve, European Central Bank, Bank of England, and Bank of Japan.

### Data sources

The sources of the data are access free and can download it, all the communique were downloaded from the BIS Central bank speeches, and for some cases, we use the specific Central Bank pages, especially for the case of Japan, more specifically for the XXX Governor.

The interest rate and the GDP growth rate were also downloaded from each Central bank. 

**Note. -** This code example is only for the case of the Bank of England.

------

##### Importing the main libraries and modules

```python
import codecs
import datetime as dt
import os
import pickle
import re
import matplotlib.pyplot as plt
```

###### For tokenizing sentences


```python
import nltk
import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm
from tone_count import *
```


```python
nltk.download("punkt")
plt.style.use("seaborn-whitegrid")
```

    [nltk_data]     Downloading package punkt to
    [nltk_data]     C:\Users\canut\AppData\Roaming\nltk_data...
    [nltk_data]     Package punkt is already up-to-date!

The ***tone_count module*** is available here at my Github page.

###### Open the Databases form pickle


```python
boe = "DB\\boe_pickle"
infile = open(boe, "rb")
boe = pickle.load(infile)
```


```python
lm = "data\\list_sent"
infile = open(lm, "rb")
lmdict = pickle.load(infile)
```


```python
neg = "data\\negate"
infile = open(neg, "rb")
negate = pickle.load(infile)
```


```python
print(len(boe))
```

    124


Measuring the elapse time, although the database is not extensive, the tone XXX  (tone_count) takes its time...


```python
import time
start = time.time()
temp = [tone_count_with_negation_check(lmdict, x) for x in boe.text]
temp = pd.DataFrame(temp)
end = time.time()
print(end - start)
```

    23.20803737640381

Next, we measure the Wordcount, the number of positive words, and the number of negative words.

```python
boe["wordcount"] = temp.iloc[:, 0].values
boe["NPositiveWords"] = temp.iloc[:, 1].values
boe["NNegativeWords"] = temp.iloc[:, 2].values
```

###### Sentiment Score normalized by the number of words.


```python
boe["sentiment"] = (
    (boe["NPositiveWords"] - boe["NNegativeWords"]) / boe["wordcount"] * 100
)

boe["Poswords"] = temp.iloc[:, 3].values
boe["Negwords"] = temp.iloc[:, 4].values
```


```python
boe.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>Index</th>
      <th>wordcount</th>
      <th>NPositiveWords</th>
      <th>NNegativeWords</th>
      <th>sentiment</th>
      <th>Poswords</th>
      <th>Negwords</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2008-01-22</th>
      <td>Speech given by Mervyn King, Governor of the B...</td>
      <td>0</td>
      <td>2292</td>
      <td>89</td>
      <td>122</td>
      <td>-1.439791</td>
      <td>[growth, more, most, largest, increasing, grow...</td>
      <td>[default, crisis, losses, collapse, losses, fe...</td>
    </tr>
    <tr>
      <th>2008-03-19</th>
      <td>Sovereign Wealth Funds and Global Imbalances S...</td>
      <td>1</td>
      <td>4047</td>
      <td>136</td>
      <td>138</td>
      <td>-0.049419</td>
      <td>[growth, higher, higher, up, benefited, most, ...</td>
      <td>[imbalances, default, questions, failings, imb...</td>
    </tr>
    <tr>
      <th>2008-03-31</th>
      <td>Extract from a speech by Mervyn King, Governor...</td>
      <td>2</td>
      <td>1482</td>
      <td>45</td>
      <td>38</td>
      <td>0.472335</td>
      <td>[more, stability, achieve, more, more, enable,...</td>
      <td>[default, interference, down, low, lower, fall...</td>
    </tr>
    <tr>
      <th>2008-04-20</th>
      <td>Monetary Policy and the Financial System Remar...</td>
      <td>3</td>
      <td>2820</td>
      <td>43</td>
      <td>107</td>
      <td>-2.269504</td>
      <td>[more, rise, rise, above, rise, transparency, ...</td>
      <td>[default, turmoil, serious, challenges, tighte...</td>
    </tr>
    <tr>
      <th>2008-06-21</th>
      <td>How Big is the Risk of Recession? Speech given...</td>
      <td>4</td>
      <td>3834</td>
      <td>150</td>
      <td>127</td>
      <td>0.599896</td>
      <td>[good, delighted, most, opportunity, valuable,...</td>
      <td>[risk, recession, default, strong, slow, weake...</td>
    </tr>
  </tbody>
</table>



```python
pl = pd.DataFrame()

pl["date"] = pd.to_datetime(boe.index.values, format="%Y-%m-%d")
pl["b"] = pl["date"].apply(lambda x: x.strftime("%Y-%m"))
print(pl["b"])
```


```python
boe = pd.merge(boe, pl, left_on="Index", right_index=True)
boe.head()
boe.info()
```



Finally, we plot the number of Positive, Negative words and the Net Sentiment index.




```python
import matplotlib.dates as mdates
```


```python
NetSentiment = boe["NPositiveWords"] - boe["NNegativeWords"]
```


```python
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
```

```python
years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")
```

format the ticks


```python
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
# Minor ticks every month.
fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
```


```python
datemin = np.datetime64(boe.date[0], "Y")
datemax = np.datetime64(boe.date[-1], "Y") + np.timedelta64(1, "Y")
# plt.xticks(range(len(pl.b)), pl.b, rotation = 'vertical',fontsize=8)
ax.set_xlim(datemin, datemax)
ax.grid(True)
plt.show()

```

![png](Analysis_preliminary_files/net.png) 



Normalize data


```python
NPositiveWordsNorm = (
    boe["NPositiveWords"] / boe["wordcount"] * np.mean(boe["wordcount"])
)
NNegativeWordsNorm = (
    boe["NNegativeWords"] / boe["wordcount"] * np.mean(boe["wordcount"])
)
NetSentimentNorm = NPositiveWordsNorm - NNegativeWordsNorm
```



#####  Loading interest rates DB


```python
boerate = pd.read_excel(r"DB/int.xlsx")
boerate["Date"] = pd.to_datetime(boerate.Date.values, format="%Y-%m-%d")
boerate.set_index(["Date"])
boerate.fillna(method="ffill", inplace=True)
boerate.info()
```


```python
selected_columns = boerate[["Date", "Official Rate"]]
rate_df = selected_columns.copy()
rate_df.rename(columns={"Official Rate": "Rate"}, inplace=True)
```


```python
datetime_series = pd.to_datetime(rate_df["Date"])
datetime_index = pd.DatetimeIndex(datetime_series.values)
rate_df = rate_df.set_index(datetime_index)
print(rate_df.index)
```


```python
fig, ax = plt.subplots(figsize=(15, 7))
plt.title("Official interest rate: United Kingdom", fontsize=16)
ax.plot(rate_df.Date, rate_df["Rate"].values, c="green", linewidth=1.0)
ax.grid(True)
plt.show()
```


![png](Analysis_preliminary_files/boe_rate.png)
    

######  Adding interest rate decision


```python
boe["RateDecision"] = None
boe["Rate"] = None
```


```python
for i in range(len(boe)):
    for j in range(len(rate_df)):
        if boe.date[i] == rate_df.Date[j]:
            boe["Rate"][i] = float(rate_df["Rate"][j + ]
```

We check for NAS, it is possible due to spare days in the communique database.


```python
boe[boe["Rate"].isna()]
boe["Rate"].fillna(method="ffill", inplace=True)
boe["RateDecision"].fillna(method="ffill", inplace=True)
```


```python
for i in range(len(boe) - 1):
    if boe["Rate"][i] == boe["Rate"][i + 1]:
        boe["RateDecision"][i] = 0
    elif boe["Rate"][i] < boe["Rate"][i + 1]:
        boe["RateDecision"][i] = 1
    elif boe["Rate"][i] > boe["Rate"][i + 1]:
        boe["RateDecision"][i] = -1
```

```python
boe.head(5)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: center;
    }

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>Index</th>
      <th>wordcount</th>
      <th>NPositiveWords</th>
      <th>NNegativeWords</th>
      <th>sentiment</th>
      <th>Poswords</th>
      <th>Negwords</th>
      <th>date</th>
      <th>b</th>
      <th>RateDecision</th>
      <th>Rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2008-01-22</th>
      <td>Speech given by Mervyn King, Governor of the B...</td>
      <td>0</td>
      <td>2292</td>
      <td>89</td>
      <td>122</td>
      <td>-1.439791</td>
      <td>[growth, more, most, largest, increasing, grow...</td>
      <td>[default, crisis, losses, collapse, losses, fe...</td>
      <td>2008-01-22</td>
      <td>2008-01</td>
      <td>-1</td>
      <td>5.50</td>
    </tr>
    <tr>
      <th>2008-03-19</th>
      <td>Sovereign Wealth Funds and Global Imbalances S...</td>
      <td>1</td>
      <td>4047</td>
      <td>136</td>
      <td>138</td>
      <td>-0.049419</td>
      <td>[growth, higher, higher, up, benefited, most, ...</td>
      <td>[imbalances, default, questions, failings, imb...</td>
      <td>2008-03-19</td>
      <td>2008-03</td>
      <td>0</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>2008-03-31</th>
      <td>Extract from a speech by Mervyn King, Governor...</td>
      <td>2</td>
      <td>1482</td>
      <td>45</td>
      <td>38</td>
      <td>0.472335</td>
      <td>[more, stability, achieve, more, more, enable,...</td>
      <td>[default, interference, down, low, lower, fall...</td>
      <td>2008-03-31</td>
      <td>2008-03</td>
      <td>0</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>2008-04-20</th>
      <td>Monetary Policy and the Financial System Remar...</td>
      <td>3</td>
      <td>2820</td>
      <td>43</td>
      <td>107</td>
      <td>-2.269504</td>
      <td>[more, rise, rise, above, rise, transparency, ...</td>
      <td>[default, turmoil, serious, challenges, tighte...</td>
      <td>2008-04-20</td>
      <td>2008-04</td>
      <td>0</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>2008-06-21</th>
      <td>How Big is the Risk of Recession? Speech given...</td>
      <td>4</td>
      <td>3834</td>
      <td>150</td>
      <td>127</td>
      <td>0.599896</td>
      <td>[good, delighted, most, opportunity, valuable,...</td>
      <td>[risk, recession, default, strong, slow, weake...</td>
      <td>2008-06-21</td>
      <td>2008-06</td>
      <td>-1</td>
      <td>5.25</td>
    </tr>
  </tbody>
</table>
</div>



#####  Save as pickle for the next part


```python
rate_des_pickle = "DB/rate_boe"
rate_des_o = open(rate_des_pickle, "wb")
pickle.dump(boe, rate_des_o)
rate_des_o.close()
```

###### In case you need save as an excel spreadsheet.


```python
boe.to_excel("E:\\GitRepo\\CB speeches\\data\\sent_BOE.xlsx",
    sheet_name="BOE", engine="xlsxwriter")
```



Finally, we prepare the code for the last graph considering each governorās period in office, also it is included the official interest rate of the Bank of England.

##### Final plot: Sentiment index and official interest rate

###### Speaker window


```python
King = np.logical_and(boe.index > "2003-07-01", boe.index < "2013-07-01")
Carney = np.logical_and(boe.index > "2013-07-01", boe.index < "2020-03-15")
Bailey = np.logical_and(boe.index > "2020-03-16", boe.index < "2028-03-16")
Speaker = np.logical_or.reduce((King, Bailey))
```

###### Moving Average


```python
Window = round(0.025 * len(boe))
CompToMA = NetSentimentNorm.rolling(Window).mean()
```


```python
cmin, cmax = None, None
if CompToMA.min() < NetSentimentNorm.min():
    cmin = CompToMA.min()
else:
    cmin = NetSentimentNorm.min()
if CompToMA.max() > NetSentimentNorm.max():
    cmax = CompToMA.max()
else:
    cmax = NetSentimentNorm.max()
```

##### Final Plotting Data


```python
import datetime
import matplotlib.dates as mdates
import matplotlib.transforms as mtransforms
```


```python
fig, ax = plt.subplots(figsize=(15, 7))
plt.title("Sentiment analysis evolution", fontsize=16)

ax.scatter(boe.date, boe["Rate"] * 15, c="blue", alpha=0.5)
ax.plot(boe.date, CompToMA, c="red", linewidth=2.0)
ax.plot(boe.date, NetSentimentNorm, c="green", linewidth=1, alpha=0.5)

ax.legend(
    [   "BOE Funds Rate", str(str(Window) + " statements moving average"),
        "Net sentiment of individual statements"
    ], prop={"size": 12}, loc=1,)

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter("%Y")

# Set X-axis and Y-axis range
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

# format the coords message box
ax.format_xdata = mdates.DateFormatter("%Y-%m-%d")
ax.grid(True)
ax.tick_params(axis="both", which="major", labelsize=12)

# Fill Speaker
trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
theta = 0.9
ax.fill_between(boe.index, 0, 10, where=Speaker, facecolor="lightblue", alpha=0.5, transform=trans)

# Add text
props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
ax.text(
    0.15,
    0.75,
    "Sir Mervyn King",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,)
ax.text(
    0.56,
    0.75,
    "Mark Carney",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,)
ax.text(
    0.92,
    0.75,
    "Andrew Bailey",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,)

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
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),)
ax.annotate(
    "QE2",
    xy=(q2, 6),
    xytext=(q2, -8),
    size=10,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),)
ax.annotate(
    "QE3",
    xy=(q3, 5),
    xytext=(q3, -9),
    size=10,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),)
ax.annotate(
    "Covid-19",
    xy=(q4, 2),
    xytext=(q4, -12),
    size=10,
    ha="right",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),)
ax.annotate(
    "CV+",
    xy=(q41, 3),
    xytext=(q41, -12),
    size=10,
    ha="left",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),)
ax.annotate(
    "CV+2",
    xy=(q42, 3),
    xytext=(q42, -12),
    size=10,
    ha="center",
    verticalalignment="bottom",
    arrowprops=dict(arrow_style, shrink=0.05, ls="--", color="gray", lw=0.5),)

plt.show()
```


![png](Analysis_preliminary_files/final.png)
    

TO QUATERLY


```python
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
```

 BOE to excel file for topics creation


```python
boe.to_excel(
    "E:\\GitRepo\\CB speeches\\data\\topic_BOE.xlsx",
    sheet_name="BOE",
    engine="xlsxwriter",
)
```
