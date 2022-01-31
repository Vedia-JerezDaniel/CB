import numpy as np
import pandas as pd
# import datetime as dt
# from dateutil.relativedelta import *
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pickle
   
   
jpn = 'DB/jpn_f'
infile = open(jpn,'rb')
jpn = pickle.load(infile)
jpn.head(10)

df = jpn[['date','Index','b','Rate','RateDecision']]
df

"""
    # The target range was changed a couple of days after the announcement in the past,
#  while it is immediately put in effect on the day recently.
# Use the target rate three days after the meeting as target announced,
#  compare it with previous day's rate to check if rate has been changed.
#   -1: Rate lower
#    0: No change
#   +1: Rate hike
    """    
    
decision_list = []
rate_diff_list = []

for j in range(len(df)):
    rate_diff_list.append(float(df['Rate'].iloc[j+3]) - float(df['Rate'].iloc[j-1]))
    if df['Rate'].iloc[j-1] == df['Rate'].iloc[j+3]:
        decision_list.append(0)
    elif df['Rate'].iloc[j-1] < df['Rate'].iloc[j+3]:
        decision_list.append(1)
    elif df['Rate'].iloc[j-1] > df['Rate'].iloc[j+3]:
        decision_list.append(-1)
        
decision_list
rate_diff_list

rate_diff_list.extend([0,0,0])

df.loc[:,'RateDiff'] = rate_diff_list
df.loc[:,'RateDecision'] = decision_list
df
    
"""
Rate Change Event
"""
# Add binary column to see if rate is changed
df['RateChanged'] = df['RateDecision'].apply(lambda x: 0 if x == 0 else 1)

sns.scatterplot(x=df.index, y=df['RateDecision'].apply(lambda x: float(x)))
plt.show()

df.to_excel("E:\\GitRepo\\CB speeches\\data\\jpn_pre.xlsx", engine='xlsxwriter')
        
"""
Add Quantitative Easing as a Lower event
Between 2008 and 2016 saw zero interest rate. Main monetary measure shifted to quantity from rate. Thus, add "lower" events when those QE was announced.
"""
    
# Add 2008-11-25 to fomc_calendar when QE was first announced but not in FOMC Calendar
# Mark RateDecision = -1 (lower) even when rate is not changed but additional quantitative measures were announced

# QE1 Announced
rec_20081125 = pd.Series([True, False, False, 'Ben Bernanke', 0, -1, -1], index=['unscheduled', 'forecast', 'confcall', 'ChairPerson', 'Rate', 'RateDiff', 'RateDecision'], name=dt.datetime.strptime('2008-11-25', '%Y-%m-%d'))

    """
    Add economic data to the df:
    Processing Potential GDP...
    Processing PCE
    Processing GDP..
    Processing CPI
    Processing Unemployemnt..
    Processing Employemnt..
    Processing ISM PMI...
    Processing ISM NMI...
    Processing Retail Sales..
    Processing Home Sales..
        """
    
    """Only the apply
    Taylor rule, and it is saved in a different Df
    """     
    