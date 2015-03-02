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

# Define parser globally
parser = argparse.ArgumentParser(description='''CP/SP Timing Analysis Plotter -
    Run this script from the same folder as the data csv's, filenames will be used for legend''')

def get_args():
    '''# Argument parser. The parser of arguments.'''
    
    parser.add_argument('-D', '--debug', action='store_true',
                        help='Enable verbose debug output to console')
    parser.add_argument('-f1', '--old_data', action='store',
                        help='The csv file for the legacy build\'s timing data.')
    parser.add_argument('-f2', '--new_data', action='store',
                        help='The csv file for the new build\'s timing data.')
    return parser.parse_args()
        

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
        # if start is the same as end, no x values or y values need to be set

        if start<end:
            x = np.arange(start,end+1)
            y = [i+offset]*len(x)
        elif start>end:
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
        labels.append(" ") # add blanks between each label to space out data
    plt.yticks(range(len(labels)),labels)
    
def show_plots():
    '''Creates legend and shows plot (specifically tuned for this graph)'''
    
    # Create legend patches using args and slicing off the .csv from the filename
    old_legend = mp.Patch(color='purple', label=args.old_data[:-4]) 
    new_legend = mp.Patch(color='blue', label=args.new_data[:-4])
    
    # Place legend (may need to be changed in later releases) and show plots
    plt.legend(handles=[new_legend, old_legend], loc='upper center')
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()
    


if __name__ == "__main__":
    args = get_args()
    
    # Try to call the args and if the first one fails, print the help and exit
    try:
        old_data = make_lol(args.old_data)
    except:
        print # Buffer line
        parser.print_help()
        exit()
    new_data = make_lol(args.new_data)
    make_plots(old_data,'purple',0.25)
    make_plots(new_data,'blue',-0.25)
    show_plots()
    