""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSX file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
import random
# %%
class plot_data(object):
    # ==============================
    # Methods for plotting dataframes
    # ==============================
    
    # Generates 1 random color by default
    # Should receives n color requests as argument
    def random_color(qty = 10):
        temp = ['#'+''.join([random.choice('0123456789ABCDEF')
                              for j in range(6)])
                 for i in range(qty)]
        return temp
    
    # Line Plot
    def line_plot(dataframe, title, ylabel):
        # Theme
        plt.style.use('fivethirtyeight')
        # Figure size
        # fig, ax = plt.subplots()
        # Format
        # locator = mdates.AutoDateLocator()
        # formatter = mdates.AutoDateFormatter(locator)
        # ax.xaxis.set_major_locator(locator)
        # ax.xaxis.set_major_formatter(formatter)
        # -
        # color1 = plot_data.random_color()
        # Set axis from data set
        # xvalues = dataframe.index.values
        # yvalues = dataframe['P Total']
        # Plot data set
        dataframe.plot(kind='line',
                       linewidth=1,
                       title=title,
                       ylabel=ylabel,
                       figsize=(10,5))
        # fig.autofmt_xdate()
        # Show graph
        plt.show()