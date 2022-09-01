""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSM file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
from loading import file_load as fl
from sorting import sort_data as sd
from plotting import plot_data as pld
# %%
# Electrical Load Data
EIE_load = fl.electric_load_file('Load','EIE_load.xlsx')
# ---
EIE_Pt = sd.filter_data(EIE_load,'P Total')
EIE_Pt = sd.date_range(EIE_Pt,'2018-04-06', '2018-04-13')
# -
EIE_Qt = sd.filter_data(EIE_load,'Q Total')
EIE_Qt = sd.date_range(EIE_Qt,'2018-04-06', '2018-04-13')
# -
EIE_PF = sd.filter_data(EIE_load,'PF Total')
EIE_PF = sd.date_range(EIE_PF,'2018-04-06', '2018-04-13')
# %%
# Weather Data
EIE_weather = fl.weather_files('Weather')
# ---
EIE_Irr = sd.filter_data(EIE_weather,'AVG Irradiance')
EIE_Irr = sd.date_range(EIE_Irr,'2021-04-09', '2021-04-16')
# -
EIE_Temp = sd.filter_data(EIE_weather,'AVG Temperature')
EIE_Temp = sd.date_range(EIE_Temp,'2021-04-09', '2021-04-16')
# -
EIE_Wind = sd.filter_data(EIE_weather,'AVG Wind Speed')
EIE_Wind = sd.date_range(EIE_Wind,'2021-04-09', '2021-04-16')
# %%
# Plotting
pld.line_plot(EIE_Pt)
pld.line_plot(EIE_Qt)
pld.line_plot(EIE_PF)
# %%
# Plotting
pld.line_plot(EIE_Irr)
pld.line_plot(EIE_Temp)
pld.line_plot(EIE_Wind)
# %%