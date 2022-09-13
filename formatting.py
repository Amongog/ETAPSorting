""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSX file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
import pandas as pd
# %%
class format_data(object):
    # ==============================
    # Methods for creating custom format dataframes
    # ==============================
    # Creates a daframe for ETAP PV simulations
    # The Dataframe fed into de method must have the required columns
    def ETAP_PV(dataframe, secondary_df):
        # Initializes Dataframe
        temp = pd.DataFrame()
        # Creates blank columns to follow format
        temp['P(MW)'] = ''
        temp['Q(Mvar)'] = ''
        temp['PF%'] = ''
        temp['V(p.u.)'] = ''
        temp['Angle'] = ''
        temp['Humidity'] = ''
        # Copies temperature data
        temp['Temp C'] = dataframe['AVG Temperature']
        temp['Wind'] = ''
        # Copies irradiance data
        temp['Irrandiance(W/m^2)'] = dataframe['AVG Irradiance']
        # Splits datetime as required
        temp['Hour'] = dataframe.index.hour
        temp['Min'] = dataframe.index.minute
        # We need seconds to be 0 to match electrical load data
        temp['Seconds'] = dataframe.shape[0]*0
        temp['Date'] = dataframe.index.date
        temp = temp.iloc[::2,:]
        temp['Date'] = secondary_df.index.date
        return temp
    
    # Creates a daframe for ETAP Lumped Load simulations
    # The Dataframe fed into de method must have the required columns
    def ETAP_Lump(dataframe):
        # Initializes Dataframe
        temp = pd.DataFrame()
        # ETAP requies MW and MVar insted of M / Var
        temp['P(MW)'] = dataframe['P Total']/1000000
        temp['Q(Mvar)'] = dataframe['Q Total']/1000000
        # Creates blank columns to follow format
        temp['PF%'] = ''
        temp['V(p.u.)'] = ''
        temp['Angle'] = ''
        temp['Humidity'] = ''
        temp['Temp C'] = ''
        temp['Wind'] = ''
        temp['Irrandiance(W/m^2)'] = ''
        # Splits datetime as required
        temp['Hour'] = dataframe.index.hour
        temp['Min'] = dataframe.index.minute
        temp['Seconds'] = dataframe.index.second
        temp['Date'] = dataframe.index.date
        return temp
    
    # Creates a daframe for HOMER simulations
    def HOMER(dataframe):
        # Initializes Dataframe
        temp = pd.DataFrame()
        # Splits datetime as required
        temp['Data'] = dataframe.resample('H').mean()
        return temp