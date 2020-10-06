import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import data_extractor as de

import subprocess
import time 
import rips
import glob
import os
from PIL import Image

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

def export_to_GT(path, name):
    wb = xlrd.open_workbook(f"resultspace/{name}/201910_TR_1.xlsx")
    sh = wb.sheet_by_index(0)
    list_data = []
    for rownum in range(sh.nrows):
        list_data.append(sh.row_values(rownum))
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body = {
                "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": f"{name}!A68:X200",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": list_data }]}
        ).execute()
                        
    df=pd.read_csv(path + f"/resultspace/{name}/sim_result.csv")
    kin = []
    for i in range(0, len(df['FOPT'])-1):
        col = []
        col.append(int(i))
        col.append(int(df['FOPT'][i]))
        kin.append(col)
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"{name}!A100:B150",
                        "majorDimension": "ROWS",
                        "values": kin}]}
        ).execute()
    
# Добавить импорт счетчика количество строк (выполненных работ) для исключения ошибок
def create_table_and_import(team_name, path):

    wb = xlwt.Workbook()
    wb.add_sheet('sheet')
    
    values = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=f'{team_name}!A8:O65',
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
        range='Teams!A1:B50',
        majorDimension='ROWS'
    ).execute()
    return values['values']

def export_snapshots(name):
    path_grid = 'workspace/SPE1'
    process = subprocess.Popen('exec ResInsight --case "%s.EGRID"' % path_grid, shell=True)
    time.sleep(5)
    resinsight = rips.Instance.find()
    case = resinsight.project.cases()[0]
    resinsight.set_main_window_size(width=400, height=150)
    property_list = ['PRESSURE', 'SOIL']
    case_path = case.file_path
    folder_name = os.path.dirname(case_path)

    dirname = os.path.join(folder_name, f"snapshots/{name}")

    if os.path.exists(dirname) is False:
        os.mkdir(dirname)

    print("Exporting to folder: " + dirname)
    resinsight.set_export_folder(export_type='SNAPSHOTS', path=dirname)

    view = case.views()[0]
    time_steps = case.time_steps()
    l = len(time_steps) - 1
    for property in property_list:
        view.apply_cell_result(result_type='DYNAMIC_NATIVE', result_variable=property)
        view.set_time_step(time_step = l)
        view.export_snapshot()

    process.kill()

    images = []
    image_paths = glob.glob(dirname + '/*')

    for path in image_paths:
        images.append(Image.open(path))