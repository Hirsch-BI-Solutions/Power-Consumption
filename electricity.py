import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import statistics
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
import datetime
import time


""" Processing time series on domestic Electric energy consumption"""

#open file
e=pd.read_csv('D202.csv')
print(e.columns)
e_df=DataFrame(e)
print(e_df)

#parse index
e_df['DATE']=pd.to_datetime(e_df['DATE'], infer_datetime_format=True)
indexeddf=e_df.set_index(['DATE'])
print(indexeddf)


#parsing to time format and extracting dates with 'created_at'
x=e_df['DATE']=pd.to_datetime(e_df['DATE'], format='%m-%d-%y')

Day=e_df['DATE'].dt.day_name()
Month=e_df['DATE'].dt.month_name()
Year=e_df['DATE'].dt.year

#subsetting timeseries
e_df['Year']=e_df['DATE'].dt.year
e_df['Month']=e_df['DATE'].dt.month_name()
e_df['Day']=e_df['DATE'].dt.day


#day_index per week 'D' 
Day_index=indexeddf.resample('D').mean()
print(Day_index)

#
Day_index.plot()

#weekly index aggregation
Week_index_w=indexeddf.resample('W').agg({'COST_dollar':'max','USAGE':'max'})
Week_index_w.plot()

#weekly index aggregation
Week_index=indexeddf.resample('W').agg({'COST_dollar':'min','USAGE':'min'})
print(Week_index.stack())

#
Week_index.plot()


#subplot intelligence

f,axes = plt.subplots(1,2, figsize=(10, 10))
C=sns.scatterplot(Week_index_w.COST_dollar    , Week_index_w.USAGE, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[0]).set_title("Weekly max of household electric consumpton")

D=sns.scatterplot(Day_index.COST_dollar , Day_index.USAGE, s=100, edgecolor='black', alpha=0.5,\
     palette='Blues',ax=axes[1]).set_title("Daily mean of household electric consumpton")

plt.show()





