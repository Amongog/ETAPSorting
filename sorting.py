""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSM file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
class sort_data(object):
    # ==============================
    # Methods for sorting dataframes
    # ==============================
    
    # Sorts dataframe by specified date range
    def date_range(dataframe,dateInit,dateEnd):
        temp = dataframe.loc[dateInit:dateEnd]
        if temp.empty:
            print('Unavailable date range selected.')
        else:
            print('---> Selection OK')
        return temp
    
    # Sorts dataframe by specified data. Up to 10 columns
    def filter_data(dataframe,d1,d2='',d3='',d4='',d5='',d6='',d7='',d8='',d9='',d10=''):
        if d2=='':
            temp = dataframe.loc[:,[d1]]
        elif d3=='':
            temp = dataframe.loc[:,[d1,d2]]
        elif d4=='':
            temp = dataframe.loc[:,[d1,d2,d3]]
        elif d5=='':
            temp = dataframe.loc[:,[d1,d2,d3,d4]]
        elif d6=='':
            temp = dataframe.loc[:,[d1,d2,d3,d4,d5]]
        elif d7=='':
            temp = dataframe.loc[:,[d1,d2,d3,d4,d5,d6]]
        elif d8=='':
            temp = dataframe.loc[:,[d1,d2,d3,d4,d5,d6,d8]]
        elif d9=='':
            temp = dataframe.loc[:,[d1,d2,d3,d4,d5,d6,d8]]
        elif d10=='':
            temp = dataframe.loc[:,[d1,d2,d3,d4,d5,d6,d8,d9]]
        else:
            temp = dataframe.loc[:,[d1,d2,d3,d4,d5,d6,d8,d9,d10]]
        return temp