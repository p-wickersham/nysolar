#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:09:36 2021

@author: patrickwickersham
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#imports darta from downloaded NYSERDA csv (copy included in dataset, opened: 5/13/21)
solar = pd.read_csv('Statewide_Solar_Projects__Beginning_2000.csv', 
                    index_col=False)

#creates a new column with the year the project was connected to the grid.
date = pd.to_datetime(solar['Interconnection Date'])
solar['year'] = date.dt.year

#creates new dateframe grouped by year
solar_by_date = solar.groupby(['year'],as_index=False).sum()

#add columns for cumulative installed capacity
#sort dataframe by year
solar_by_date.sort_index(inplace=True)
solar_by_date['Cum Installed Capacity'] = solar_by_date['PV System Size (kWac)'].cumsum()           
solar_by_date['Cum Storage Capacity'] = solar_by_date['Energy Storage System Size (kWac)'].cumsum()


#divide by 1000 to convert from kWac to MWac
solar_by_date['tot_pv_install (MWac)'] = solar_by_date['Cum Installed Capacity']/1000
solar_by_date['tot_storage (MWac)'] = solar_by_date['Energy Storage System Size (kWac)']/1000
solar_by_date['pv_storage_ratio (MWac)'] = solar_by_date['tot_storage (MWac)'] / solar_by_date['tot_pv_install (MWac)']

#%% Graph total pv capacity installed and total storage capacity installed 



fig,(ax1,ax2) = plt.subplots(1,2,dpi=300)
fig.suptitle('Ratio of Installed PV and PV-coupled Storage Capacity')
solar_by_date.reset_index().plot.scatter(x='year',y='tot_pv_install (MWac)',ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('Total PV Install (MWac)')
solar_by_date.reset_index().plot.scatter(x='year',y='tot_storage (MWac)',ax=ax2)
ax2.set_xlabel('Year')
ax2.set_ylabel('Total PV-Coupled Storage (MWac)')
fig.savefig('solar_storage_cap_growth.png', dpi=300)
fig.tight_layout()

#%% Graph Installed PV to Storage ratio
fig,ax1 = plt.subplots(dpi=300)
fig.suptitle('Ratio of PV and PV-coupled Storage Capacity')
solar_by_date.reset_index().plot.scatter(x='year',y='pv_storage_ratio (MWac)',ax=ax1)
ax1.set_xlabel('year')
ax1.set_ylabel('Total PV Capacity/PV-Coupled Storage Ratio')
fig.savefig('ratio_PV_storage.png', dpi=300)
fig.tight_layout()


