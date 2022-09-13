""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSX file following ETAP formatting, so it can be used in simulations with this software.
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
    def filter_data(dataframe,col1,col2='',col3='',col4='',col5='',col6='',col7='',col8='',col9='',col10=''):
        if col2=='':
            temp = dataframe.loc[:,[col1]]
        elif col3=='':
            temp = dataframe.loc[:,[col1,col2]]
        elif col4=='':
            temp = dataframe.loc[:,[col1,col2,col3]]
        elif col5=='':
            temp = dataframe.loc[:,[col1,col2,col3,col4]]
        elif col6=='':
            temp = dataframe.loc[:,[col1,col2,col3,col4,col5]]
        elif col7=='':
            temp = dataframe.loc[:,[col1,col2,col3,col4,col5,col6]]
        elif col8=='':
            temp = dataframe.loc[:,[col1,col2,col3,col4,col5,col6,col8]]
        elif col9=='':
            temp = dataframe.loc[:,[col1,col2,col3,col4,col5,col6,col8]]
        elif col10=='':
            temp = dataframe.loc[:,[col1,col2,col3,col4,col5,col6,col8,col9]]
        else:
            temp = dataframe.loc[:,[col1,col2,col3,col4,col5,col6,col8,col9,col10]]
        return temp