#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 15:23:10 2021

@author: patrickwickersham
"""

def nyiso_csv(filename):
    import pandas as pd
    rtd = pd.read_csv(filename)
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