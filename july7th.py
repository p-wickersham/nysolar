#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:14:08 2021

@author: patrickwickersham
"""

import pandas as pd

rtd = pd.read_csv('OASIS_Real_Time_Dispatch_Actual_Load_2010.csv')
date = pd.to_datetime(rtd['RTD End Time Stamp'])
rtd['date'] = date
year = date.dt.year 
day = date.dt.day
time = date.dt.time
hour = date.dt.hour
minute = date.dt.minute
rtd['time'] = time
rtd['year'] = year
rtd['day'] = day
rtd['hour'] = hour
rtd['minute'] = minute
#rtd = rtd.set_index('date')
rtd['RTD'] = rtd['RTD Actual Load']
tot5min = rtd.groupby('date').RTD.sum()
tot5min = tot5min.rename('Total')
tot5min['time'] = tot5min['date'].dt.time

stat5min = tot5min.groupby('time')['Total'].describe()
stat5min = stat5min.set_index(['date','time'])

#%%
tot5min = rtd.groupby('date').RTD.sum()
tot5min = tot5min.rename('Total')
tot5min['time'] = tot5min['date'].dt.time

stat5min = tot5min.groupby('time')['Total'].describe()
stat5min = stat5min.set_index(['date','time'])

tot5min = rtd.resample('5T', on='date').RTD.sum()
mean5min = tot5min.resample('D', kind='timestamp').RTD.mean()

test = rtd.groupby([pd.Grouper(key='date',freq='5T'),'Zone Name']).RTD.sum()

#%% Create interactive html chart
import seaborn as sns
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(30, 12)})
sns.set_style("darkgrid")

import plotly.express as px
fig=px.bar(test,x=test.index, 
                 y='Total', 
                 title='Average Daily Load Profile: April 2010'
                 )
fig.update_xaxes(rangeslider_visible=True)
fig.show()
fig.write_html("load.html")



