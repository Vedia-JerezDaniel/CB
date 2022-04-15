import numpy as np
from numpy.lib.function_base import diff
import pandas as pd
import datetime as dt

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1 import host_subplot

def fortay(sheet_name):
    df = pd.read_excel("EDA/eda_q.xlsx", sheet_name=sheet_name)
    # Create taylor dataframe
    taylor = df.copy(deep=True)
    # Obtain available index used to calculate Taylor rule each day
    taylor['Y-Yp'] = (((taylor['GDP'] - taylor['GDP Pot']).rolling(window=4).sum())/4)/taylor['GDP'].rolling(window=4).mean()
    taylor['Y-Yp'] = taylor['Y-Yp'].fillna(method='bfill')
    taylor['Pi*'] = 2
    taylor['Pi-Pi*'] = taylor['CPI'] - taylor['Pi*'].rolling(window=4).mean()
    taylor['Pi-Pi*'] = taylor['Pi-Pi*'].fillna(method='bfill')
    taylor['r'] = 0.5
    # Calculate Taylor Rule
    taylor['Taylor'] = taylor['r'] + taylor['CPI'] + 0.5 * taylor['Pi-Pi*'] + 0.5 * taylor['Y-Yp']
    # taylor['Taylor'] = taylor['Taylor'].nfillna(method='bfill')
    # Calculate Balanced-approach Rule
    taylor['Balanced'] = (taylor['r'] + taylor['CPI'] + 0.5 * taylor['Pi-Pi*'] + taylor['Y-Yp']).map(lambda x: max(x, 0))
    taylor.replace(taylor.Balanced.max(), taylor.Taylor.max(), inplace=True)
    # Calculate Inertia Rule
    taylor['Inertia'] = 0.85 * taylor['inter_rate'] - 0.15 * taylor['Balanced']
    # Drop unnecessary columns
    # taylor = taylor.drop(columns = ['CPI', 'Pi*', 'Pi-Pi*', 'r'])
    db = taylor[['Taylor', 'Inertia', 'Balanced']]

    taylor['Taylor-Rate'] = taylor['Taylor'] - taylor['inter_rate']
    taylor['Balanced-Rate'] = taylor['Balanced'] - taylor['inter_rate']
    taylor['Inertia-Rate'] = taylor['Inertia'] - taylor['inter_rate']

    taylor['Taylor_diff'] = taylor['Taylor'].diff(1)
    taylor['Balanced_diff'] = taylor['Balanced'].diff(1)
    taylor['Inertia_diff'] = taylor['Inertia'].diff(1)

    return taylor

uk = fortay(0)
jpn = fortay(1)
us = fortay(2)
euro = fortay(3)

taylor = us
taylor['Taylor'].head(5)

uk.to_excel("E:\\GitRepo\\CB speeches\\EDA\\uktaylor.xlsx", engine="xlsxwriter")


euro.date = pd.to_datetime(euro.date)
jpn.date = pd.to_datetime(jpn.date)

ax1 = host_subplot(111)
# ax2 = ax1.twinx()
ax1.set_xlabel('date')
ax1.set_ylabel('Taylor \n CPI', color="black")
# ax2.set_ylabel('Inertia', color='r')
l1, =ax1.plot(jpn['date'],jpn['Taylor'], 'bo-',label='Taylor')
l2, =ax1.plot(jpn['date'],jpn['CPI'], 'g*--',label='CPI')
# l3, =ax2.plot(taylor['date'], taylor['Inertia'], 'r--',label='Inertia')
leg = plt.legend(loc=0, ncol=2, borderaxespad=0.)
ax1.yaxis.get_label().set_color(l1.get_color())
leg.texts[0].set_color(l1.get_color())
# ax1.yaxis.get_label().set_color(l2.get_color())
# leg.texts[1].set_color(l2.get_color())
# ax2.yaxis.get_label().set_color(l3.get_color())
# leg.texts[2].set_color(l3.get_color())
plt.show()

(euro)


# ARIMA FINAL
import warnings
from pmdarima import auto_arima
from sklearn import metrics
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
warnings.filterwarnings("ignore")

def timeseries_evaluation_metrics_func(y_true, y_pred):
    
    def mean_absolute_percentage_error(y_true, y_pred): 
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    print('Evaluation metric results:-')
    print(f'MSE is : {metrics.mean_squared_error(y_true, y_pred)}')
    print(f'MSE is : {metrics.mean_absolute_error(y_true, y_pred)}')
    print(f'RMSE is : {np.sqrt(metrics.mean_squared_error(y_true, y_pred))}')
    print(f'MAPE is : {mean_absolute_percentage_error(y_true, y_pred)}')
    print(f'R2 is : {metrics.r2_score(y_true, y_pred)}',end='\n\n')
    
    
# SARIMA
# train = us.Taylor[0:-3]
# test = us.Taylor[-4:]  'unemploy', 'Construct', 'Manuf', 'Retail', 'housing', 'inter_rate',
    #    'GDP', 10 Year Treasury'

X = jpn[['CPI']]
actualtrain, actualtest = X[:-3], X[-4:]
exoX = np.log(jpn[['BDI']])
exotrain, exotest = exoX[:-3], exoX[-4:]

# [1, 4,7,12]  exogenous =exotrain 
for m in [1, 4,7,12]:
    print("="*100)
    print(f' Fitting SARIMAX for Seasonal value m = {str(m)}')
    stepwise_model = auto_arima(actualtrain,exogenous =exotrain,start_p=1, start_q=1,
    max_p=7, max_q=7, seasonal=True,start_P=1,start_Q=1,max_P=7,max_D=7,max_Q=7,m=m,
    d=None,D=None, trace=True,error_action='ignore',suppress_warnings=True, stepwise=True, 
    n_jobs=4)

    print(f'Model summary for  m = {str(m)}')
    print("-"*100)
    stepwise_model.summary()

    forecast,conf_int = stepwise_model.predict(n_periods=4,exogenous =exotest, return_conf_int=True)
    df_conf = pd.DataFrame(conf_int,columns= ['Upper_bound','Lower_bound'])
    df_conf["new_index"] = range(56,60)
    df_conf = df_conf.set_index("new_index")
    forecast = pd.DataFrame(forecast, columns=['close_pred'])
    forecast["new_index"] = range(56,60)
    forecast = forecast.set_index("new_index")

    timeseries_evaluation_metrics_func(actualtest, forecast)

    import matplotlib.pyplot as plt
    plt.rcParams["figure.figsize"] = [9, 7]
    plt.plot(actualtrain, label='Train ')
    plt.plot(actualtest, label='Test ')
    plt.plot(forecast, label=f'Predicted with m={str(m)} ')
    plt.plot(df_conf['Upper_bound'], label='Confidence Interval Upper bound ')
    plt.plot(df_conf['Lower_bound'], label='Confidence Interval Lower bound ')
    plt.legend(loc='best')
    plt.show()
    print("-"*100)
    print(f' Diagnostic plot for Seasonal value m = {str(m)}')

    stepwise_model.plot_diagnostics()
    plt.show();
    print("-"*100)



X = us[['CPI']]
actualtrain, actualtest = X[:-3], X[-4:]
exoX = us[['CPI energy']]
us['CPI energy'].interpolate(method ='linear', limit_direction ='forward', limit = 5, inplace = True)
exotrain, exotest = exoX[:-3], exoX[-4:]

m = 12
print("="*100)
print(f' Fitting SARIMAX for Seasonal value m = {m}')
stepwise_model = auto_arima(actualtrain, exogenous = exotrain ,start_p=1, start_q=1,
max_p=7, max_q=7, seasonal=True,start_P=1,start_Q=1,max_P=7,max_D=7,max_Q=7,m=m,
d=None,D=None, trace=True,error_action='ignore',suppress_warnings=True, stepwise=True, 
n_jobs=4)

print(f'Model summary for  m = {m}')
print("-"*100)
stepwise_model.summary()

forecast,conf_int = stepwise_model.predict(n_periods=4, exogenous =exotest ,return_conf_int=True)
df_conf = pd.DataFrame(conf_int,columns= ['Upper_bound','Lower_bound'])
df_conf["new_index"] = range(56,60)
df_conf = df_conf.set_index("new_index")
forecast = pd.DataFrame(forecast, columns=['close_pred'])
forecast["new_index"] = range(56,60)
forecast = forecast.set_index("new_index")

timeseries_evaluation_metrics_func(actualtest, forecast)

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [9, 7]
plt.plot(actualtrain, label='Train ')
plt.plot(actualtest, label='Test ')
plt.plot(forecast, label=f'Predicted with m={m} ')
plt.plot(df_conf['Upper_bound'], label='Confidence Interval Upper bound ')
plt.plot(df_conf['Lower_bound'], label='Confidence Interval Lower bound ')
plt.legend(loc='best')
plt.show()
print("-"*100)
print(f' Diagnostic plot for Seasonal value m = {m}')

stepwise_model.plot_diagnostics()
plt.show();
print("-"*100)


us.columns