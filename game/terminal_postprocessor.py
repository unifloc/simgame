import pandas as pd
import os
import sys
import numpy
import datetime
import openpyxl


current_dir = os.getcwd()

df=pd.read_csv(current_dir + "/resultspace/ФОН/sim_result.csv")


names=df.columns[1:]
wellnames=[]
for n in names:
    a=n.split(':')
    b=a[1]
    if b in wellnames:
        break
    else:
        wellnames.append(b)
print(wellnames)