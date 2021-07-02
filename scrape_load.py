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
    rtd = (pd.read_csv('OASIS_Real_Time_Dispatch_Actual_Load_2010.csv'))
    date = pd.to_datetime(rtd['RTD End Time Stamp'])
    rtd['date'] = date
    year = date.dt.year 
    rtd['year'] = year

#
# Creates dataframe for load
#

#???? Can I make the dataframe name equal to the year in the data set?    
    RTD = rtd.pivot(index='date',
                    columns='Zone Name',
                    values='RTD Actual Load')
    RTD['Total'] = RTD.sum(axis=1)
    return RTD


#
# Creates dataframe for ramp rate between 5min intervals.
#

def calc_ramp(dataframe):

#???? Can I make the dataframe name equal to the year in the data set? 
    ramp_rate = dataframe.diff()

    return ramp_rate