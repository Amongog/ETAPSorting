""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSX file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
from loading import file_load as fl
from sorting import sort_data as sd
from plotting import plot_data as pld
from exporting import export_data as xd
# %%
# Electrical Load Data
# 1 Weeks worth of data, from 2018-06-06 to 2018-04-13 (Fri-Fri)
EIE_load = fl.electric_load_file(filePath='Load',fileName='EIE_load.xlsx')
# ---
EIE_Pt = sd.filter_data(dataframe=EIE_load, col1='P Total')
# -
EIE_Qt = sd.filter_data(dataframe=EIE_load, col1='Q Total')
# -
EIE_PF = sd.filter_data(dataframe=EIE_load, col1='PF Total')
# -
EIE_PQ = sd.filter_data(dataframe=EIE_load, col1='P Total', col2='Q Total')
# %%
# Weather Data
# Around 9 months of data in 2021
EIE_weather = fl.weather_files(filePath='Weather')
# ---
# Data range needs to match April 2nd week (Fri-Fri) for similarity with electrical load data
# Sample hours must start at 14:20 of the 1st day and end at 14:10 of the last day
# to match the time ranges of the electrical load data samples
EIE_Irr = sd.filter_data(dataframe=EIE_weather,col1='AVG Irradiance')
EIE_Irr = sd.date_range(dataframe=EIE_Irr, dateInit='2021-04-09T14:20', dateEnd='2021-04-16T14:10')
# -
EIE_Temp = sd.filter_data(dataframe=EIE_weather,col1='AVG Temperature')
EIE_Temp = sd.date_range(dataframe=EIE_Temp, dateInit='2021-04-09T14:20', dateEnd='2021-04-16T14:10')
# -
EIE_Wind = sd.filter_data(dataframe=EIE_weather,col1='AVG Wind Speed')
EIE_Wind = sd.date_range(dataframe=EIE_Wind, dateInit='2021-04-09T14:20', dateEnd='2021-04-16T14:10')
# -
EIE_Temp_Irr = sd.filter_data(dataframe=EIE_weather,col1='AVG Temperature', col2='AVG Irradiance')
EIE_Temp_Irr = sd.date_range(dataframe=EIE_Temp_Irr, dateInit='2021-04-09T14:20', dateEnd='2021-04-16T14:10')
# %%
# Plotting
pld.line_plot(dataframe=EIE_Pt, title='Electrical Load Data', ylabel='Active Power (W)')
pld.line_plot(dataframe=EIE_Qt, title='Electrical Load Data', ylabel='Reactive Power (Var)')
pld.line_plot(dataframe=EIE_PF, title='Electrical Load Data', ylabel='Power Factor')
# %%
# Plotting
pld.line_plot(dataframe=EIE_Irr, title='Weather Data', ylabel='Irradiance (W/m²)')
pld.line_plot(dataframe=EIE_Temp, title='Weather Data', ylabel='Temperature (°C)')
pld.line_plot(dataframe=EIE_Wind, title='Weather Data', ylabel='Wind Speed (m/s)')
# %%
# Exporting Full Dataframe
xd.export(dataframe=EIE_load, title='EIE_load.csv')
xd.export(dataframe=EIE_load, title='EIE_load.xlsx')
# %%
# Exporting Dataframe to ETAP format
xd.export_ETAP(dataframe=EIE_PQ, secondary_df=EIE_load, title='Lump1.xlsx', Lump=True)
# Dates for the weather data are altered and forced to match the electrical load date range
# This is required so that ETAP accepts both datasets and use them in the simulation
xd.export_ETAP(dataframe=EIE_Temp_Irr, secondary_df=EIE_load, title='PV1.xlsx', PV=True)
# %%
xd.export_HOMER(dataframe=EIE_Pt, title='HOMER.csv')