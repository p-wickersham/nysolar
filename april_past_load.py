#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:02:25 2021

@author: patrickwickersham
"""

import pandas as pd


RTD = pd.read_csv("OASIS_Real_Time_Dispatch_Actual_Load_2021.csv")

# creates datetime dtype column RTD['date'] AND callable columns 
#for year,month,day,hour,and minute

date = pd.to_datetime(RTD['RTD End Time Stamp'])
#year = date.dt.year
#month = date.dt.month
#day = date.dt.day
#hour = date.dt.hour
#minute = date.dt.minute
#second = date.dt.second
#RTD['PTID'] = RTD['Zone PTID']
#RTD['rtd_load'] = RTD['RTD Actual Load']
RTD['date'] = date
#RTD['second'] = second
#RTD['minute'] = minute
#RTD['hour'] = hour
#RTD['day'] = day
#RTD['month'] = month
#RTD['year'] = year

RTD_2020_april = RTD.pivot(index='date',
         columns='Zone Name',
         values='RTD Actual Load')


#%% add a Total column
RTD_2020_april['Total'] = RTD_2020_april.sum(axis=1)


#%% compute ramp rate


ramprate_2020_april = RTD_2020_april.diff()

