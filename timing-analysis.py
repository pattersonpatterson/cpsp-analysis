# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 13:06:43 2014

@author: derpson
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
import csv

# Take data from csv file and put into list of lists
# Format: msg#, msg name, start time, end time
def make_lol(filename):
    '''Take a csv filename and return a list of lists from the data'''
    lol = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lol.append(row)
    return lol
        


def make_plots(data,color,offset):
    '''Takes data in the form of list of lists
    Format: msg#, msg name, start time, end time
    Also takes a color corresponding to the data to set the data apart
    Also takes numerical offset, moving the data up or down'''
    i=0
    labels = []
    for num,name,start,end in data:
        print name,start,end
        if start<end:
            print name
            x = np.arange(int(start),int(end)+1)
            y = [i+offset]*len(x)
        else:
            x = np.arange(0,int(end)+1)
            x1 = np.arange(int(start),1001)
            y = [i+offset]*len(x)
            y1 = [i+offset]*len(x1)
        i+=1
        plt.plot(x,y,color=color,linewidth=4)
        try:
            plt.plot(x1,y1,color=color,linewidth=4)
        except NameError:
            pass
        labels.append(str(name))
    plt.yticks(range(len(labels)),labels)
    



# Check that the start time is less than the end time
# If so, create a numpy array from start time to finish
# If not, create 2 numpy arrays, one from 0 to start, one from finish to 1000
# Perhaps add these new arrays to DataFrame?
# y will be index +/- 0.5
# y-ticks should be replaced by msg
# x-label should be milliseconds
# Plot all on same graph with lines, set line-width=10

if __name__ == "__main__":
    old_data = make_lol('./data1.csv')
    new_data = make_lol('./data2.csv')
    make_plots(old_data,'blue',0.25)
    make_plots(new_data,'purple',-0.25)
    plt.show()