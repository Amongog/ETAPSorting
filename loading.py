""""
@author: Samuel Berrocal Soto

This code written for thesis work.

The script aims to sort out weather data and parse it in a
.XLSM file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
import os
import pandas as pd
# %%
# ==============================
# Loading files functions
# ==============================
# Makes relative path
def get_path(filePath):
    dir = os.path.dirname(__file__)
    # The last <''> is added so a final backlash <\> is added to the path in Windows
    temp = os.path.join(dir,'Measurements',filePath,'')
    return temp

# 1. Loads load measurements in a df
# 2. Merges Date & Time column and sets it as index and renames it
# 3. Renames column hearders
def electric_load_file(filePath,fileName):
    # Loading
    path = get_path(filePath)
    os.chdir(path)
    print(path)
    temp = pd.read_excel(fileName, parse_dates=[['Date','Time']])
    # Formating
    temp = temp.set_index('Date_Time')
    temp.index = pd.to_datetime(temp.index, infer_datetime_format=True)
    temp.index.names = ['Full Date']
    # Renames column hearders
    rename_load_cols(temp)
    return temp

# 1. Loads all weather measurements files in a folder to a df
# 2. Filters out unnamed, empty columns
# 3. Formats index Date as Datetimes & renames it
# 4. Renames column hearders
def weather_files(filePath):
    # Loading
    path = get_path(filePath)
    print(path)
    allFiles = [file for file in os.listdir(path) if file.endswith('.xlsx')]
    temp = pd.concat([pd.read_excel(path + file, skiprows=1) for file in allFiles], ignore_index=True)
    # Filter
    temp = temp[temp.columns.drop(list(temp.filter(regex='Unnamed:')))]
    # Formating
    temp = temp.set_index('Date')
    temp.index = pd.to_datetime(temp.index, yearfirst=True)
    temp.index.names = ['Full Date']
    # Renames column hearders
    rename_weather_cols(temp)
    return temp

# Renames column headers
def rename_load_cols(dataframe):
    dataframe.columns = ['P L1','ABS P L1','P L2','ABS P L2','P L3','ABS P L3','P Total','ABS P Total','Q L1','Q L2','Q L3','Q Total','S L1','S L2','S L3','S Total','PF L1','ABS PF L1','PF L2','ABS PF L2','PF L3','ABS PF L3','PF Total','ABS PF Total','D L1','D L2','D L3','D Total','E L1','E L2','E L3','E Total','IL1','IL2','IL3','I NEUTRAL']

# Renames column headers
def rename_weather_cols(dataframe):
    dataframe.columns = ['Err Code','AVG Wind Speed','AVG Wind Direction','AVG Temperature','AVG Relative Humidity','AVG Atmospheric Pressure','AVG Irradiance','AVG Dew Point','MIN Wind Speed','MAX Wind Speed','MIN Wind Direction','MAX Wind Direction','MIN Temperature','MAX Temperature','MIN Relative Humidity','MAX Relative Humidity','MIN Atmospheric Pressure','MAX Atmospheric Pressure','MIN Irradiance','MAX Irradiance','MIN Dew Point','MAX Dew Point']

# %%
# Testbench
# EIE_load = electric_load_file('Load','EIE_load.xlsx')
# EIE_weather = weather_files('Weather')
# %%
