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






#%%
#
# preliminary graphing
#

import seaborn as sns
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(30, 12)})
sns.set_style("darkgrid")
import plotly.express as px

# try area
fig = px.area(RT_2010_D, facet_col='Zone Name', facet_col_wrap=2)
fig.write_html("load2020.html")

#??? DatetimeIndex object is not callable in below fig
import plotly.express as px
fig=px.line(RT_2010_D, x=RT_2010_D.index(), 
                 y='RTD Actual', 
                 title='RTD 5min by 5min Ramp Rate'
                 )
fig.update_xaxes(rangeslider_visible=True)
fig.show()
fig.write_html("load.html")



#%%
#
# Now trying to figure out how to call the objects I want from all of these 
# dataframes to create more useful smaller datasets.
#

from functools import reduce
import pandas as pd
from pandas import ExcelWriter



RT_2010_D.to_csv("april_load.csv")
RT_2011_D.to_excel("april_load.xlsx", sheet_name=RT_2011_D)
RT_2012_D.to_excel("april_load.xlsx", sheet_name=RT_2012_D)
RT_2013_D.to_excel("april_load.xlsx", sheet_name=RT_2013_D)
RT_2014_D.to_excel("april_load.xlsx", sheet_name=RT_2014_D)
RT_2015_D.to_excel("april_load.xlsx", sheet_name=RT_2015_D)
RT_2016_D.to_excel("april_load.xlsx", sheet_name=RT_2016_D)
RT_2017_D.to_excel("april_load.xlsx", sheet_name=RT_2017_D)
RT_2018_D.to_excel("april_load.xlsx", sheet_name=RT_2018_D)
RT_2019_D.to_excel("april_load.xlsx", sheet_name=RT_2019_D)
RT_2020_D.to_excel("april_load.xlsx", sheet_name=RT_2020_D)
RT_2021_D.to_excel("april_load.xlsx", sheet_name=RT_2021_D)


#%%
#
# Create a frequency index to use to call specific times of day
#


#RTD_merged = reduce(lambda left,right: pd.merge(left,right,on=None,
#                                                how='outer'),data_frames)

yr = ['10','11','12','13','14','15','16','17','18','19','20','21']
for year in yr:
    index = []
    daterange = pd.date_range(f'20{year}-04-01 00:05:00', periods=30,freq='D')
    index = index.append(daterange)


for frame in dataa_frames:
    for index, value in frame.items():