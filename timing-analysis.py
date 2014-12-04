# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 13:06:43 2014

@author: derpson
"""

# Imports
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import csv
import argparse

# Argument parser. The parser of arguments.
parser = argparse.ArgumentParser(description='CP/SP Timing Analysis Plotter')
parser.add_argument('-D', '--debug', action='store_true',
                    help='Enable verbose debug output to console')
parser.add_argument('-f1', '--file1', action='store_true', default='./data1.csv',
                    help='First CSV file for analysis.')
parser.add_argument('-f2', '--file2', action='store_true', default='./data2.csv',
                    help='Second CSV file for analysis.')
args = parser.parse_args()

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
        if start==end: # if start is the same as end, increment row and skip loop
            i+=2
            continue
        elif start<end:
            x = np.arange(start,end+1)
            y = [i+offset]*len(x)
        else:
            x = np.arange(0,end+1)
            x1 = np.arange(start,1001)
            y = [i+offset]*len(x)
            y1 = [i+offset]*len(x1)
        i+=2
        plt.plot(x,y,color=color,linewidth=7)
        try:
            plt.plot(x1,y1,color=color,linewidth=7)
        except NameError:
            pass
        
        # Create Label
        labels.append(str(num)+" "+str(name))
        labels.append(" ")
    plt.yticks(range(len(labels)),labels)
    


if __name__ == "__main__":
    old_data = make_lol(args.file1)
    new_data = make_lol(args.file2)
    make_plots(old_data,'purple',0.25)
    make_plots(new_data,'blue',-0.25)
    
    old_legend = mp.Patch(color='purple', label='R3B') # Change label for data
    new_legend = mp.Patch(color='blue', label='R4')
    plt.legend(handles=[new_legend, old_legend], loc='upper center')
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()
