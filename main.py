""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSM file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
from loading import file_load as fl
from sorting import sort_dataframe as sd
# %%
EIE_load = fl.electric_load_file('Load','EIE_load.xlsx')
EIE_weather = fl.weather_files('Weather')
# %%
EIE_load_1 = sd.filter_data(EIE_load,'P Total','Q Total','PF Total')
EIE_weather_1 = sd.filter_data(EIE_weather,'AVG Irradiance','AVG Temperature')
# %%
EIE_load_1 = sd.date_range(EIE_load_1,'2018-04-09', '2018-04-10')
EIE_weather_1 = sd.date_range(EIE_weather_1,'2021-04-05', '2018-04-06')