import operator
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

plt.style.use("bmh")


df = pd.read_excel("E:\\GitRepo\\CB speeches\\EDA\\eda_q.xlsx", sheet_name="EU")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
df.dropna(inplace=True)
df.head()

# print(df['JPN'].describe())

df.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
plt.show()


cat = [f for f in df.columns]


def anova(frame):
    anv = pd.DataFrame()
    anv["features"] = cat
    pvals = []
    for c in cat:
        samples = []
        # for cls in frame[c].unique():
        s = frame["inter_rate"].values
        r = frame[c].values
        samples.append(r)
        samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv["pval"] = pvals
    return anv.sort_values("pval")


s = df["inter_rate"].values

sns.set(rc={"figure.figsize": (11.7, 8.27)})
k = anova(df)
k["disparity"] = np.log(1 / k["pval"].values)
sns.barplot(data=k, x="features", y="disparity")
plt.xticks(rotation=40)
plt.title("Disparity index")
plt.show()

# Que es disparity

# CORRELACION

individual_features_df = []
for i in range(len(df.columns) - 1):  # -1 because the last column is SalePrice
    tmpDf = df[[df.columns[i], "inter_rate"]]
    tmpDf = tmpDf[tmpDf[df.columns[i]] != 0]
    individual_features_df.append(tmpDf)

all_correlations = {
    feature.columns[0]: feature.corr()["inter_rate"][0]
    for feature in individual_features_df
}
all_correlations = sorted(all_correlations.items(), key=operator.itemgetter(1))
for (key, value) in all_correlations:
    print("{:>15}: {:>15}".format(key, value))

golden_features_list = [key for key, value in all_correlations if abs(value) >= 0.5]
print(
    "There is {} strongly correlated values with SalePrice:\n{}".format(
        len(golden_features_list), golden_features_list
    )
)

corr = df.corr()
# plt.figure(figsize=(12, 10))
sns.heatmap(
    corr[(corr >= 0.4) | (corr <= -0.4)],
    cmap="BrBG",
    vmax=1.0,
    vmin=-1.0,
    linewidths=0.1,
    annot=True,
    annot_kws={"size": 7},
)
plt.xticks(rotation=40)
plt.title("Correlation matrix")
plt.show()
