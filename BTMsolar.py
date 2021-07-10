#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:24:57 2021

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

grouped = solar.groupby('County').sum()
print(grouped)




import matplotlib.pyplot as plt
fig, axs = plt.subplots(figsize=(12,4))
RT_2010_D.groupby(RT_2010_D['date'].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel('Minutes of the day of the day')
plt.ylabel('RTD load MW')
