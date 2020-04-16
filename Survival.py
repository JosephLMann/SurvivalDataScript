#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script takes in a CSV meta data file (see Santi Correa for example)
Output is a CSV ready for PRISM 
"""

import argparse
import os
import sys
import subprocess
import numpy as np
import pandas as pd
import datetime as dt
import io
import glob

__author__ = "Joseph Mann"
__credits__ = ["Joseph Mann"]
__version__ = "0.0.1"
__maintainer__ = "Joseph Mann"
__email__ = "jlmann@stanford.edu"
__status__ = "Development"

# Function decomposition
def outPutFromMeta(fileName):
    """
    input:
    fiileName, string, fileName with .csv in it
    outputName, string, name of the csv for the survival data
    output:
    string, complete filename of the output survival csv
    """
    return fileName[:fileName.rfind('/')+1] + 'survival.csv'

def meta2survival_treatment(fileName, startDate, endDate, treatment, mouseID):
    """
    input:
    filename, string, full filename of the metaCSV
    startDate, string, metaCSV column header for the starting date used for survival
    endDate, string, metaCSV column header for the death date used for survival
    treatment, string, metaCSV column header for the treatment label. keyword argument, default is 'treatment'
    mouseID, string, metaCSV column header for the mouse.id label. keyword argument, default is 'mouse.id'
    
    output:
    csv, survival.csv ready for prism in the same folder fileName is stored in
    """
#import data and prep first dataframe
    metaDF = pd.read_csv(fileName) #import as Data Frame
    for el in [startDate,endDate]: #convert surfvival dates to datefrime, be weary of date format
        metaDF[el] = pd.to_datetime(metaDF[el], format='%m/%d/%y', errors = 'ignore')
    metaDF['deathTime'] = metaDF[endDate] - metaDF[startDate] #survival time
#prepare output survival dataframe
    unique_deaths = sorted(list(metaDF['deathTime'].unique())) #list of unique days till death
    column_names  = list(metaDF[treatment].unique()) #gets unique treatment groups for final CSV
    column_names.insert(0,'days') #upates columns to include days
    column_names.insert(0, mouseID ) #upates columns to include mouseID
    column_names.insert(0,treatment) #upates columns to include treatment
    OutputDF = pd.DataFrame(columns = column_names) #dataframe to output for final CSV
# Transfer metaDF to OutputDF
    for i in metaDF.index: #iterate through rows in the dataframe
        #  metaDF.at[i,treatment] : 1 populates a 1 in the correct treatment group, after updating the death and the correct mouseID
        OutputDF = OutputDF.append({mouseID : metaDF.at[i,mouseID] , treatment : metaDF.at[i,treatment] ,'days' : metaDF.at[i,'deathTime'] , metaDF.at[i,treatment] : 1} , ignore_index=True)
    outputDF = OutputDF.sort_values(by=[treatment,'days']) #sorts so appears in the correct order
    outputDF.to_csv(outPutFromMeta(fileName))


#Main Arguments
def main():    
    meta2survival_treatment(fileName, startDate, endDate, treatment, mouseID)

if __name__ == '__main__':
    """executed when run from command line"""
    parser = argparse.ArgumentParser(description='Survival Data Tool')

    # Positional Arguments
    parser.add_argument('fileName',
                        help="this is the full filename for your MetaFile",
                        type =str)
    parser.add_argument('startDate',
                        help="column header for the starting date used for survival in the meta csv",
                        type =str)
    parser.add_argument('endDate',
                        help="column header for the ending date used for survival in the meta csv",
                        type =str)

    # Keyword Arguments
    parser.add_argument('-m', '--mouseID',
                        help="column header for the mouseID in the meta csv",
                        type =str,
                        dest = 'mouseID',
                        default='mouse.id')

    parser.add_argument('-t', '--treatment',
                        help="column header for the treatment in the meta csv",
                        type =str,
                        dest = 'treatment',
                        default='treatment')
       
    #put positional arguments into variables
    args = parser.parse_args()
    fileName = args.fileName
    startDate = args.startDate
    endDate = args.endDate
    #put keyword arguments into variables
    mouseID = args.mouseID
    treatment = args.treatment
    main()
