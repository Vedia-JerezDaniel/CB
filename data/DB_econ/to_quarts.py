import pandas as pd

df = pd.read_excel (r'quarterly.xlsx', sheet_name='interbank')
print (df)

df["time"] = pd.to_datetime(df.time, format='%m-%d-%Y')

df.time = pd.to_datetime(df.time)
df.set_index('time', inplace=True)
df.head()

dm = df.resample('1M').mean()
dm.head()

dm['Japan'] = dm[['Japan']].interpolate(method="linear")
dm['United Kingdom'] = dm[['United Kingdom']].interpolate(method="linear")
dm['United States'] = dm[['United States']].interpolate(method="linear")
dm['Euro area (19 countries)'] = dm[['Euro area (19 countries)']].interpolate(method="linear")

dm.to_excel("quaterly_cl.xlsx", sheet_name='interbank') 

#### HOME SALES

df = pd.read_excel (r'quarterly.xlsx', sheet_name='Home sales')

dm['UK'] = dm[['UK']].interpolate(method="linear")
dm['UE'] = dm[['UE']].interpolate(method="linear")

with pd.ExcelWriter('quaterly_cl.xlsx', engine='openpyxl', mode='a') as writer:  
    dm.to_excel(writer, sheet_name='UE home sales')

### HOME SALES JAPAN To month data

df = pd.read_excel (r'quarterly.xlsx', sheet_name='home japan')
df["year"] = pd.to_datetime(df.year, format='%Y')

df.year = pd.to_datetime(df.year)
df.set_index('year', inplace=True)
df.head()
df=df.drop(['ori'], axis=1)

dm = df.resample('1M').mean()
dm.head()

dm['sales'] = dm[['sales']].interpolate(method="linear")
dm['base'] = dm[['base']].interpolate(method="linear")

with pd.ExcelWriter('quaterly_cl.xlsx', engine='openpyxl', mode='a') as writer:  
    dm.to_excel(writer, sheet_name='JP home sales')
    
## INTERBANK ALL COUNTRIES econbase FOR EDA
df = pd.read_excel (r'EDA.xlsx', sheet_name='interbank')
df["year"] = pd.to_datetime(df.date, format='%m-%d-%Y')

df.year = pd.to_datetime(df.year)
df.set_index('year', inplace=True)
df.head()
df=df.drop(['date'], axis=1)

dm = df.resample('1M').mean()
dm.head()

dm['JPN'] = dm[['JPN']].interpolate(method="linear")
dm['UK'] = dm[['UK']].interpolate(method="linear")
dm['US'] = dm[['US']].interpolate(method="linear")
dm['EU_19'] = dm[['EU_19']].interpolate(method="linear")

with pd.ExcelWriter('EDA.xlsx', engine='openpyxl', mode='a') as writer:  
    dm.to_excel(writer, sheet_name='interbank_m')
    
## TO QUATERLY

df = pd.read_excel (r'quarterly.xlsx', sheet_name='EU poten')
df["year"] = pd.to_datetime(df.Country, format='%Y')

df.set_index('year', inplace=True)
df.head()
df=df.drop(['Country'], axis=1)

dm = df.resample('Q').mean()
dm.head()

dm['quarter'] = dm.index.to_period('Q')


dm['Pot'] = dm[['Euro area']].interpolate(method="linear")

with pd.ExcelWriter('quarterly.xlsx', engine='openpyxl', mode='a') as writer:  
    dm.to_excel(writer, sheet_name='EU Potential')
