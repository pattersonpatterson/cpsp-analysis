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
    '''Take a csv filename and return a list of lists from the data
    (Requires import csv)'''
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
    
    # Use i for the y-values    
    i=0
    labels = []
    for num,name,start,end in data:
        start,end = int(start),int(end) # typecast data as int
        
        # Check whether the start time is less than end time; handle accordingly
        if start<end:
            x = np.arange(start,end+1)
            y = [i+offset]*len(x)
        else:
            x = np.arange(0,end+1)
            x1 = np.arange(start,1001)
            y = [i+offset]*len(x)
            y1 = [i+offset]*len(x1)
        i+=1
        plt.plot(x,y,color=color,linewidth=7)
        try:
            plt.plot(x1,y1,color=color,linewidth=7)
        except NameError:
            pass
        
        # Create Label
        labels.append(str(num)+" "+str(name))
    plt.yticks(range(len(labels)),labels)
    


if __name__ == "__main__":
    old_data = make_lol('./data1.csv')
    new_data = make_lol('./data2.csv')
    make_plots(old_data,'blue',0.20)
    make_plots(new_data,'purple',-0.20)
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()