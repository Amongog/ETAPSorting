""""
@author: Samuel Berrocal Soto

This project was written for thesis work.

The project aims to sort out weather data and parse it in a
.XLSX file following ETAP formatting, so it can be used in simulations with this software.
"""
# %%
from loading import file_load as fl
from formatting import format_data as fd
import os
from xlsxwriter.utility import xl_rowcol_to_cell
# %%
class export_data(object):
    # ==============================
    # Methods for exporting dataframes
    # ==============================
    # Creates a CSV/Excel file with the whole dataframe
    def export(dataframe, title):
        # Creates folders if non exist
        path = fl.set_path('Exported','Full')
        os.makedirs(path, exist_ok=True)
        # Sets output file name
        output = os.path.join(path, title)
        # Checks desired file extension
        if '.csv' in title:
            dataframe.to_csv(output)
        elif '.xlsx' in title:
            dataframe.to_excel(output)
        else:
            print('--> ERROR: Requested output format is invalid (!!!)')
    
    # Creates a CSV/Excel file with the ETAP format
    def export_ETAP(dataframe, secondary_df, title, PV=False, Lump=False):
        # Creates folders if non exist
        path = fl.set_path('Exported','ETAP')
        os.makedirs(path, exist_ok=True)
        # Sets output file name
        output = os.path.join(path, title)
        # Checks which type of format is required
        if PV:
            # Creates formatted dataframe
            pv_df = fd.ETAP_PV(dataframe, secondary_df)
            # Checks correct file extension
            if '.csv' in title:
                print('--> ERROR: ETAP requires .xlsx files (!!!)')
            elif '.xlsx' in title:
                pv_df.to_excel(output, index=False)
            else:
                print('--> ERROR: Requested output format is invalid (!!!)')
        elif Lump:
            # Creates formatted dataframe
            lump_df = fd.ETAP_Lump(dataframe)
            # Checks correct file extension
            if '.csv' in title:
                print('--> ERROR: ETAP requires .xlsx files (!!!)')
            elif '.xlsx' in title:
                lump_df.to_excel(output, index=False)
            else:
                print('--> ERROR: Requested output format is invalid (!!!)')
        else:
            print('--> ERROR: No ETAP format selected (!!!)')
    
    # Creates a CSV/Excel with plain format
    # This format is required for HOMER simulations
    def export_HOMER(dataframe, title):
        # Creates folders if non exist
        path = fl.set_path('Exported','HOMER')
        os.makedirs(path, exist_ok=True)
        # Sets output file name
        output = os.path.join(path, title)
        # Creates formatted dataframe
        homer_df = fd.HOMER(dataframe)
        # Checks desired file extension
        if '.csv' in title:
            homer_df.to_csv(output, header=False, index=False)
        elif '.xlsx' in title:
            homer_df.to_excel(output, header=False, index=False)
        else:
            print('--> ERROR: Requested output format is invalid (!!!)')