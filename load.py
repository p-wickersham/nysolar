#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 13:16:25 2021

@author: patrickwickersham
"""
import scrape_load as sl
###!!! IF STATEMENT TO ITERATE THROUGH THESE FILES AND COMBINE THEM


#
#It ain't pretty but it gets the job done...kinda
#

RT_2010_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2010.csv')
ramp_2010_rate = sl.calc_ramp(RT_2010_D)

RT_2011_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2011.csv')
ramp_2011_rate = sl.calc_ramp(RT_2011_D)

RT_2012_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2012.csv')
ramp_2012_rate = sl.calc_ramp(RT_2012_D)

RT_2013_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2013.csv')
ramp_2013_rate = sl.calc_ramp(RT_2013_D)

RT_2014_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2014.csv')
ramp_2014_rate = sl.calc_ramp(RT_2014_D)

RT_2015_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2015.csv')
ramp_2015_rate = sl.calc_ramp(RT_2015_D)

RT_2016_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2016.csv')
ramp_2016_rate = sl.calc_ramp(RT_2016_D)

RT_2017_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2017.csv')
ramp_2017_rate = sl.calc_ramp(RT_2017_D)

RT_2018_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2018.csv')
ramp_2018_rate = sl.calc_ramp(RT_2018_D)

RT_2019_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2019.csv')
ramp_2019_rate = sl.calc_ramp(RT_2019_D)

RT_2020_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2020.csv')
ramp_2020_rate = sl.calc_ramp(RT_2020_D)

RT_2021_D = sl.read_loadfile('OASIS_Real_Time_Dispatch_Actual_Load_2021.csv')
ramp_2021_rate = sl.calc_ramp(RT_2021_D)

from functools import reduce
import pandas as pd

data_frames = [RT_2010_D, RT_2011_D, RT_2012_D, RT_2013_D, RT_2014_D, 
               RT_2015_D, RT_2016_D, RT_2016_D, RT_2017_D, RT_2018_D, 
               RT_2019_D, RT_2020_D, RT_2021_D]
RTD_merged = reduce(lambda left,right: pd.merge(left,right,on=None,
                                                how='outer'),data_frames)



