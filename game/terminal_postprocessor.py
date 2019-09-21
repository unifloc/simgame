import pandas as pd
import os
import sys
import numpy
import datetime
import openpyxl


current_dir = os.getcwd()



def make_month_report(team_name):
    path_to_team_directory  = current_dir + "/resultspace/" + team_name + "/"
    df = pd.read_csv(path_to_team_directory + "sim_result.csv")
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

    time=pd.to_datetime(df.time)
    report=pd.DataFrame()

    report['Time']=time

    for name in wellnames:
        report[name + '. Дебит по нефти, м3/сут']=df['WOPR:'+name]
        report[name + '. Дебит по воде, м3/сут']=df['WWPR:'+name]
        report[name + '. Дебит по жидкости, м3/сут']=df['WLPR:'+name]
        report[name + '. Дебит по газу, м3/сут']=df['WGPR:'+name]
        report[name + '. Закачка воды, м3/сут']=df['WWIR:'+name]

    print(report.tail())

    report.resample('M', on='Time').mean()

    report.to_excel(path_to_team_directory + "МЭР {}.xlsx".format(team_name), sheet_name='МЭР'.format(team_name))

team_names = ['ФОН', "FlexOil"]
for this_team_name in team_names:
    make_month_report(this_team_name)