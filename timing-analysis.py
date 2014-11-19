# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 13:06:43 2014

@author: derpson
"""

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Take data from excel spreadsheet and put into DataFrame


# Separate DataFrames into two: one for each release


# Check that the start time is less than the end time
# If so, create a numpy array from start time to finish
# If not, create 2 numpy arrays, one from 0 to start, one from finish to 1000
# Perhaps add these new arrays to DataFrame?
# y will be index +/- 0.5
# y-ticks should be replaced by msg
# x-label should be milliseconds
# Plot all on same graph with lines, set line-width=10