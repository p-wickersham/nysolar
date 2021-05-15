#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:42:43 2021

@author: patrickwickersham
"""
The objective of this repository is to quantify the growth in PV


#insolar.py
The dataset used in this analysis was downloaded as a csv file from the 
following website:  https://der.nyserda.ny.gov/search/ 
/!\ The copy saved in this repository was downloaded on 5/13/21 selecting for
 energy storage and pv projects, leaving all other options on default. /!\

##Modules Need:
pandas
matplotlib.pyplot
numpy

After saving that csv in the working directory, **insolar.pv** will read 
that csv file into the a pandas dataframe.

lines 18-19 create a new column denoting the year the project was brought online.

line 22 and lines 26-34 create a copy of the original dataframe with cumulative totals for 
capacituy installed each year.

The final two blocks of code graph the cumulative total installed capacity 
for solar panels (left) and  storage (right), with the third graphic 
illustrating the ratio of installed storage capacity divided by installed 
PV capacity.  This gives us a rough estimate of how resilient the new york 
state grid remains as new sources of variable generation come online.


##Future additions
1) join capacity installed to a county-level shapefile to illustrate the 
locations of PV and storage installations to get a better idea of where these
technologies are being installed and if and location specific congestion 
issues might arise on the grid.