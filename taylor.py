import numpy as np
import pandas as pd
import datetime as dt

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1 import host_subplot

import pickle

def fortay(sheet_name):
    df = pd.read_excel("EDA/eda_q.xlsx", sheet_name=sheet_name)
    # Create taylor dataframe
    taylor = df.copy(deep=True)
    # Obtain available index used to calculate Taylor rule each day
    taylor['Y-Yp'] = (taylor['GDP'] - taylor['GDP Pot'])
    taylor['Pi*'] = 2
    taylor['Pi-Pi*'] = taylor['CPI'] - taylor['Pi*']
    taylor['r'] = 2

    # Calculate Taylor Rule
    taylor['Taylor'] = taylor['r'] + taylor['CPI'] + 0.5 * taylor['Pi-Pi*'] + 0.5 * taylor['Y-Yp']
    # Calculate Balanced-approach Rule
    taylor['Balanced'] = (taylor['r'] + taylor['CPI'] + 0.5 * taylor['Pi-Pi*'] + taylor['Y-Yp']).map(lambda x: max(x, 0))
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

euro.to_excel("E:\\GitRepo\\CB speeches\\EDA\\eutaylor.xlsx", engine="xlsxwriter")



ax1 = host_subplot(111)
ax2 = ax1.twinx()
ax1.set_xlabel('date')
ax1.set_ylabel('Taylor \n Balanced', color='b')
ax2.set_ylabel('Inertia', color='r')
l1, =ax1.plot(taylor['date'], taylor['Taylor'], 'b-',label='Taylor')
l2, =ax1.plot(taylor['date'], taylor['Balanced'], 'g*--',label='Balanced')
l3, =ax2.plot(taylor['date'], taylor['Inertia'], 'r--',label='Inertia')
leg = plt.legend()
ax1.yaxis.get_label().set_color(l1.get_color())
leg.texts[0].set_color(l1.get_color())
ax1.yaxis.get_label().set_color(l2.get_color())
leg.texts[1].set_color(l2.get_color())
ax2.yaxis.get_label().set_color(l3.get_color())
leg.texts[2].set_color(l3.get_color())
plt.show()





