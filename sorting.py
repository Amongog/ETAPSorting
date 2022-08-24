""""
@author: Samuel Berrocal Soto

This code written for thesis work.

The script aims to sort out weather data and parse it in a
.XLSM file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
import os
import pandas as pd
import matplotlib.pyplot as plt
# %%
# Functions for the script
def get_path(measurePath):
    dir = os.path.dirname(__file__)
    # The last <''> is added so a final backlash <\> is added to the path in Windows
    temp = os.path.join(dir,'Measurements',measurePath,'')
    return temp

def load_single(measurePath,fileName):
    path = get_path(measurePath)
    os.chdir(path)
    print(path)
    temp = pd.read_excel(fileName)
    return temp

def load_multi(measurePath):
    path = get_path(measurePath)
    print(path)
    allFiles = [file for file in os.listdir(path) if file.endswith('.xlsx')]
    temp = pd.concat([pd.read_excel(path + file) for file in allFiles], ignore_index=True)
    return temp
    
# %%
# Testbench
load = load_single('Load','EIE_load.xlsx')
weather = load_multi('Weather')
weather.rename(columns=weather.iloc[0], inplace=True)
weather.drop(weather.index[0], inplace = True)
weather.drop(weather.index[0], inplace = True)
# %%