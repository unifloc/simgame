from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

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
        
    result = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body = {
                "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": f"{name}!A68:X200",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": list_data}]}
        ).execute()
    print(list_data)
                        
    
# Добавить импорт счетчика количество строк (выполненных работ) для исключения ошибок
def create_table_and_import(team_name, path):

    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet')
    
    values = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=f'{team_name}!A8:P15',
        majorDimension='ROWS'
    ).execute()
    ranges = values.get('valueRanges', [])

    row = 7
    col = 0
    style1 = xlwt.XFStyle()
    style1.num_format_str = 'd mmm yyyy'
    style2 = xlwt.XFStyle()
    style2.num_format_str = '#,##0'
    for item in ranges:
        val = item['values']
        for i in range(0,5):
            for j in range(0,15):
                if (j == 1 & i != 0):
                    ws.write(row, col, val[i][j], style1)
                elif (j > 4 & j != 11):
                    ws.write(row, col, val[i][j], style2)
                else:
                    ws.write(row, col, val[i][j])
                col += 1
            col = 0
            row += 1

    wb.save(path + f'/dataspace/{team_name}/Мероприятия РиЭНМ {team_name}.xls')
    print('Значения успешно импортированы')
    return

def import_teamnames():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='Teams!A1:B2',
        majorDimension='ROWS'
    ).execute()
    return values['values']

