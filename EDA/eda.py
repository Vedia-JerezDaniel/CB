import operator
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

plt.style.use("bmh")


df = pd.read_excel("E:\\GitRepo\\CB speeches\\EDA\\eda_q.xlsx", sheet_name="JPN")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
df.dropna(inplace=True)
df.head()

# print(df['JPN'].describe())

df.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
# plt.title('Variables histogram')
plt.show()


# por ver
# sns.histplot(df['unemploy'], kde=True, palette='deep')
# plt.show()

# for i in range(0, len(df.columns), 5):
#     sns.pairplot(data=df, x_vars=df.columns[i:i+4], y_vars=['inter_rate'])
# plt.show()

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
# CAMBIAR NOMBRES
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

corr = df.corr()  # We already examined SalePrice correlations
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


# features_to_analyse = [x for x in golden_features_list]
# features_to_analyse.append('inter_rate')

# fig, ax = plt.subplots(2, 2, figsize = (18, 12))
# for i, ax in enumerate(fig.axes):
#     if i < len(features_to_analyse) - 1:
#         sns.regplot(x=features_to_analyse[i],y='inter_rate', data=df[features_to_analyse], ax=ax)
# plt.show() # correr al final no junto al anterior

# HACER PARA LOS NEGATIVOS

# df.dropna(inplace=True)

## CROSS TABLES

db = pd.read_excel("E:\GitRepo\CB speeches\EDA\eda_q.xlsx", sheet_name="cross")
db["date"] = pd.to_datetime(db["date"])
db = db.set_index("date")
db.head()

columns_to_show = ["CPI", "GDP growth", "inter_rate", "unemploy"]
db.groupby(["country"])[columns_to_show].agg([np.mean, np.std, np.min, np.max])

for column in db.columns:
    sns.boxplot(y=column, x="country", data=db)
    plt.show()


# -------------------
def corrmessage(df, features_to_analyse):
    for col in features_to_analyse:
        pearson_coef, p_value = stats.pearsonr(df[col], df["inter_rate"])
        print(
            "The PearsonR between {} and interest rate is {} with a P-value of P = {}".format(
                col, pearson_coef, p_value
            )
        )
        if p_value < 0.001:
            print(
                "Correlation between {} and interest rate is statistically significant..".format(
                    col
                )
            )
        elif p_value < 0.05:
            print(
                "Correlation between {} and interest rate is statistically moderate..".format(
                    col
                )
            )
        elif p_value < 0.1:
            print(
                "Correlation between {} and interest rate is statistically weak..".format(
                    col
                )
            )
        else:
            print(
                "Correlation between {} and interest rate is statistically not significant..".format(
                    col
                )
            )
        if pearson_coef > 0:
            if pearson_coef > 0.85:
                print(
                    "Coeff ~{} shows that the relationship is positive and very strong.\n".format(
                        pearson_coef
                    )
                )
            elif pearson_coef > 0.75:
                print(
                    "Coeff ~{} shows that the relationship is positive and quite strong.\n".format(
                        pearson_coef
                    )
                )
            elif pearson_coef > 0.60:
                print(
                    "Coeff ~{} shows that the relationship is positive and moderately strong.\n".format(
                        pearson_coef
                    )
                )
            elif pearson_coef > 0.50:
                print(
                    "Coeff ~{} shows that the relationship is positive and only moderate.\n".format(
                        pearson_coef
                    )
                )
            else:
                print(
                    "Coefficient ~{} shows that the relationship is positive and weak.\n".format(
                        pearson_coef
                    )
                )
        else:
            if abs(pearson_coef) > 0.85:
                print(
                    "Coeff ~{} shows that the relationship is negative and very strong.\n".format(
                        pearson_coef
                    )
                )
            elif abs(pearson_coef) > 0.75:
                print(
                    "Coeff ~{} shows that the relationship is negative and quite strong.\n".format(
                        pearson_coef
                    )
                )
            elif abs(pearson_coef) > 0.60:
                print(
                    "Coeff ~{} shows that the relationship is negative and moderately strong.\n".format(
                        pearson_coef
                    )
                )
            elif abs(pearson_coef) > 0.50:
                print(
                    "Coeff ~{} shows that the relationship is negative and only moderate.\n".format(
                        pearson_coef
                    )
                )
            else:
                print(
                    "Coefficient ~{} shows that the relationship is negative and weak.\n".format(
                        pearson_coef
                    )
                )


corrmessage(df, features_to_analyse)
