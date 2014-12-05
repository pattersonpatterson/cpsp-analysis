cpsp-analysis
=============

Uses excel spreadhseet data exported to csv to visualize message timing from 0 to 1000 milliseconds.

To run:
=======

1. Ensure that Python is installed on your workstation
2. Download and unzip (or clone) this git repository
3. In a terminal window, navigate to the location of the cloned git repository and run `pip install requirements.txt` to ensure that dependencies have been installed
4. Follow the instructions [here](http://info.amc.faa.gov/wiki/index.php/Running_the_CP_SP_timing_analysis_tools) and at the top of the included Excel workbook to fill out the table of data and export the spreadsheets to .csv files
5. Once the Excel spreadsheets have been exported to .csv, open a terminal and run `python timing-analysis.py -f1 [legacy_data.csv] -f2 [release_data.csv]`
 
**NOTE**: Give the csv files descriptive names. These names will be used as the legend in the final plot.

# Example

Example data is included in this repository. You can generate the graph by running `python timing-analysis.py -f1 'WFO 3B.csv' -f2 'WFO 4.csv'`
