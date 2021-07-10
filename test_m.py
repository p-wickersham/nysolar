#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:46:11 2021

@author: patrickwickersham
"""
#
# import csv and datetime colums
#
import pandas as pd

rtd = pd.read_csv('OASIS_Real_Time_Dispatch_Actual_Load_2010.csv')
date = pd.to_datetime(rtd['RTD End Time Stamp'])
rtd['date'] = date
year = date.dt.year 
day = date.dt.day
hour = date.dt.hour
minute = date.dt.minute
rtd['year'] = year
rtd['day'] = day
rtd['hour'] = hour
rtd['minute'] = minute

#
# call values by time of day (Boolean Masking)
#
hours = [0,24]
for hours in day:
    minute = 5
    for 
    a = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 5) ]
    a = a.groupby('Zone Name').mean()
    HB_0_mean_load[f'{n}']
    minute = minute + 5
    
    b = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 10) ]
    b = b.groupby('Zone Name').mean()
    c = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 15) ]
    c = c.groupby('Zone Name').mean()
    d = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 20) ]
    d = d.groupby('Zone Name').mean()
    e = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 25) ]
    e = e.groupby('Zone Name').mean()
    f = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 30) ]
    f = f.groupby('Zone Name').mean()
    g = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 35) ]
    g = g.groupby('Zone Name').mean()
    h = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 40) ]
    h = h.groupby('Zone Name').mean()
    i = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 45) ]
    i = i.groupby('Zone Name').mean()
    j = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 50) ]
    j = j.groupby('Zone Name').mean()
    k = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 55) ]
    k = k.groupby('Zone Name').mean()
    l = rtd[ (rtd['hour'] == n) & (rtd['minute'] == 00) ]
    l = l.groupby('Zone Name').mean()



TEST = test.pivot(index='date',
                    columns='Zone Name',
                    values='RTD Actual Load')
RTD['Total'] = RTD.sum(axis=1)

RTD1 = rtd.pivot(index='date',
                 columns='Zone Name',
                 values='RTD Actual Load')

#%% Create interactive html chart
import seaborn as sns
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(30, 12)})
sns.set_style("darkgrid")

import plotly.express as px
fig=px.histogram(ramprate_2020_april,x=ramprate_2020_april.index, 
                 y=['CAPITL'], 
                 title='RTD Actual Load'
                 )
fig.update_xaxes(rangeslider_visible=True)
fig.show()
fig.write_html("load.html")
