#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:18:34 2021

@author: patrickwickersham
"""
import pandas as pd

#
# Set up function for reading files. Returns a set of dataframes
#

def read_loadfile(filename):
    rtd = pd.read_csv(filename)
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
    return rtd
#
# Creates dataframe for load
#
'''
#???? Can I make the dataframe name equal to the year in the data set?    
    RTD = rtd.pivot(index='date',
                    columns='Zone Name',
                    values='RTD Actual Load')
    RTD['Total'] = RTD.sum(axis=1)
    return RTD

#
# Creates dataframe for ramp rate between 5min intervals.
#
'''
def calc_ramp(dataframe):
    rr = dataframe.pivot(index='date',
                          columns='Zone Name',
                          values='RTD Actual Load')
#???? Can I make the dataframe name equal to the year in the data set? 
    ramp_rate = rr.sum(axis=1)

    return ramp_rate
