# -*- coding: utf-8 -*-
"""



"""
import os
import pandas as pd


filename = 'example_file_2013-07-25.xlsx'
filepath = os.path.join(os.getcwd(), filename)
sheet = 'min'


### this fails:
df_in = pd.read_excel(filepath, sheet, skiprows=11, header=10, index_col=1)

### workaround

import myexcel as mx

xlsall = mx.ExcelFile(filename)

### this reads the data in, 
### BUT stills uses the first row above the data with the units as column names

df_corr =xlsall.parse(sheet, skiprows=11, header=10, index_col=1)

df_corr.columns


### check dedicated 1904 file



filename_1904 = 'example_file_2013-07-25_1904-dates.xlsx'
filepath_1904 = os.path.join(os.getcwd(), filename_1904)
sheet = 'min'


df_in_1904 = pd.read_excel(filepath_1904, sheet, skiprows=11, 
                      header=10, index_col=1)