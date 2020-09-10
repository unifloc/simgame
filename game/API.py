from pprint import pprint
import numpy as np
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import data_extractor as de

# Производим авторизацию в API

CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '17O_GghnChsKLxtdRGGWG8W9aOMx411DRHKszuMPflMo'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Создаем таблицу и импортируем значения
import xlwt
import xlrd
from xlutils.copy import copy

def export_to_GT(name):
    wb = xlrd.open_workbook("201910_TR_1.xlsx")
    sh = wb.sheet_by_index(0)
    list_data = []
    for rownum in range(sh.nrows):
        list_data.append(sh.row_values(rownum))
    #list_data.append(sh.col_values(12))
    
    result = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body = {
                "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": f"{name}!A68:X200",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": list_data }]}
        ).execute()
                        
    sh1 = wb.sheet_by_index(1)
    kin = []
    kin.append(sh1.row_values(0))
    result = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body = {
                "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": f"{name}!B46:B100",
         "majorDimension": "ROWS",
         "values": kin}]}
        ).execute()
    
# Добавить импорт счетчика количество строк (выполненных работ) для исключения ошибок
def create_table_and_import(team_name, path):

    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet')
    
    values = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=f'{team_name}!A8:P25',
        majorDimension='ROWS'
    ).execute()
    ranges = values.get('valueRanges', [])

    for item in ranges:
        val = item['values']
    df1 = pd.DataFrame(val)
    path_to_table = path + f'/dataspace/{team_name}/Мероприятия РиЭНМ {team_name}.xlsx'
    de.append_df_to_excel(path_to_table, df1,sheet_name='sheet1',
                            startrow=7, startcol=0, index=False, header=False)

    return

def import_teamnames():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='Teams!A1:B2',
        majorDimension='ROWS'
    ).execute()
    return values['values']


# import pandas as pd
# #import xlwings as xw
# import xlsxwriter as xlsw

# values = service.spreadsheets().values().batchGet(
#     spreadsheetId=spreadsheet_id,
#     ranges='ФОН!A8:P25',
#     majorDimension='ROWS'
# ).execute()
# ranges = values.get('valueRanges', [])
# for item in ranges:
#     val = item['values']
# df1 = pd.DataFrame(val, columns=())
# #df1['Perf'] = df1.astype(int)
# print(df1)

# import data_extractor as de
# de.append_df_to_excel("test.xlsx", df1,sheet_name='Лист1',
#                             startrow=0, startcol=0, index=False, header=False)
#writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

#df1.to_excel(writer, sheet_name="TR",startrow=30, startcol=0, header=False, index=False)
# wb=xw.Book('test.xlsx')
# data_excel = wb.sheets['TR']
# data_pd = data_excel.range('A1:X100').options(pd.DataFrame, header = 1, index = False).value
# print (data_pd)
