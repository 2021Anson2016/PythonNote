
#encoding=utf8
# for python2.7
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

## for >= python 3.4
import sys
import importlib
importlib.reload(sys)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





Destop = 'C:\\Users\\AnsonHsu\\Desktop\\uLED\\'
rawDataName = 'rawdata_csv.csv'
df_raw = pd.read_csv(Destop + rawDataName) # df = pd.read_excel( Destop + fileName)
# print(df_raw)

rawDataName = 'rawdata_csv.csv'
selectGroupName = 'SelectGroup_Anson.csv'
df_SelGroup = pd.read_csv(Destop + selectGroupName)
print(df_SelGroup)
