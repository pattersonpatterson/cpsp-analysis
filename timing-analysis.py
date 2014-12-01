# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 13:06:43 2014

@author: derpson
"""

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Take data from excel spreadsheet and put into DataFrame (declared globally)


# Separate DataFrames into two: one for each release


# Check that the start time is less than the end time
# If so, create a numpy array from start time to finish
# If not, create 2 numpy arrays, one from 0 to start, one from finish to 1000
# Perhaps add these new arrays to DataFrame?
# y will be index +/- 0.5
# y-ticks should be replaced by msg
# x-label should be milliseconds
# Plot all on same graph with lines, set line-width=10


'''Possible outline:
for row in dataframe:
    if start_time < end time:
        x = np.arange(start_time,end_time+1)
        y = [row]*len(x)
    else:
        x = np.arange(0,start_time+1)
        x1 = np.arange(end_time,1001)
        y = [row]*len(x)
        y1 = [row]*len(x1)
    
    if release == old:
        offset = -0.5
        color = purple
    else:
        offset = 0.5
        color = blue
        
    y = [num+offset for num in y] # possibly send to function

    plt.plot(x and y,color=color,linewidth=10)
    if(x1 exists):
        y1 = [num+offset for num in y1]
        plt.plot(x1 and y1,color=color,linewidth=10)
        # delete the x1/y1 variables at the end to clean up
        del x1,y1

        
# after all rows have been processed, fix the labels and show
Set the labels to the msg type
plt.show()'''
