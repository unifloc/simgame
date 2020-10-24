# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 05:02:49 2018

@author: Rinat Khabibullin
"""

import pandas as pd
import numpy as np

keywords = ['WELSPECS','COMPDAT','WCONPROD','WCONINJE','TSTEP']
GROUP = 'G1'
DEPTH = '1*'
DIAM = 0.2

# TODO проверить правильность синтаксиса для OPM
# TODO сделать перевод в ППД
# TODO разобраться с ГНО
# TODO правильно ли перфорирует, учитывается ли прошлая перфорация?

class WellParam:
    """
    store all well params at last date in schedule file
    need to get skin for enchancement acounting
    """
    def __init__(self,name,x=1,y=1,z1=1,z2=1):
        self.x = x
        self.y = y
        self.z1 = z1
        self.z2 = z2
        self.group = GROUP
        self.phase = "OIL"
        self.type = 'PROD'
        self.status_perf = "OPEN"
        self.status_work = 'OPEN'
        self.kh = "1*"
        self.skin = 0
        self.diam = DIAM
        self.cf = "1*"
        self.filttablenum = "1*"
        self.depth = "1*"
        self.lrat = 10
        self.bhp = 50
        self.control = 'BHP'
        self.pump = 'Насос 100-500'


class Schedule:
    """
    schcedule reader and parser
    generate list (dicr) of wells in schedule file with params at last date
    """
    def __init__(self, fname):
        self.keys = []
        self.lastkey = []
        self.wells = {}             # well dict
        self.read_file(fname)       # read and parse file
        for l in self.keys:
            self.read_key(l[0],l)   # read keys and params

    def read_file(self, name):
        """
        read file 
        break all file content into keywords for further analysis
        """
        try:
            file = open(name)
        except:
            print('error reading file ' + name)
            return
        # delete leading and trailing spaces and \n from file
        self.content = [line.rstrip('\n') for line in file]
        self.content = [line.strip() for line in self.content]
        keyread = False
        for line in self.content:
            if line[:2] == '--':            # comment in file detected
                continue
            if line == 'SCHEDULE':          # section title ignored
                print('SCHEDULE section detected')
                continue
            if line in keywords:            # looking only keywords of interest
                print('keyword '+ line +' detected')
                self.lastkey = []           # start collecting keyword params
                self.lastkey.append(line)
                keyread = True
                continue
            if line == '/':                 # end of keyword found
                if keyread:                 # stop collecting if started before
                    self.keys.append(self.lastkey)
                keyread = False
                continue
            if keyread:
                line=line.replace('2*',' 1* 1* ')
                line=line.replace('3*',' 1* 1* 1* ')
                line=line.replace('4*',' 1* 1* 1* 1* ')
                line=line.replace('5*',' 1* 1* 1* 1* 1* ')
                if len(line) > 2:           # ignore short lines (blank lines)
                    self.lastkey.append(line)
        if keyread:
            self.keys.append(self.lastkey)

        print('reading '+name+' done: ' +str(len(self.keys)) +' keywords detected')
        pass

    def read_key(self, key, lines):
        """
        read params from keywords
        store in wells dictionary 
        """
        if lines[0] != key :
            s = 'error parsing ' +key+ '. No ' +key+ ' keyword'
            print(s)
            return s
        for line in lines: 
            if line == key:
                continue
            if len(line) < 2:
                continue
            if key == 'TSTEP':      #ignored at the moment 
                continue
            if line[-1:] != '/':
                print('Warning: ' + key+ 'string has no end character \ ')
            line = line.split('/')[0]
            params = line.split()   # split data line into parama
            wellname = params[0]    # first in line is well name
            if wellname in self.wells:   
                w = self.wells[wellname]
            else:
                w = WellParam(wellname)
                self.wells[wellname] = w
            if key == 'COMPDAT':
                if params[3] != '1*':
                    w.z1 = int(params[3])
                if params[4] != '1*':
                    w.z2 = int(params[4])
                if params[5] != '1*':
                    w.status_perf = params[5]
                if params[8] != '1*':
                    w.diam = params[8]
                if params[10] != '1*':
                    w.skin = float(params[10])
                continue
            if key == 'WCONPROD':
                if params[1] != '1*':
                    w.status_work = params[1]
                if params[2] != '1*':
                    w.control = params[2]
                if params[6] != '1*':
                    w.lrat = float(params[6])
                if params[8] != '1*':
                    w.bhp = float(params[8])
                w.type = 'PROD'
                continue
            if key == 'WCONINJE':
                if params[1] != '1*':
                    w.phase = params[1]
                if params[2] != '1*':
                    w.status_work = params[2]
                if params[3] != '1*':
                    w.control = params[3]
                if params[4] != '1*':
                    w.lrat = float(params[4])
                if params[6] != '1*':
                    w.bhp = float(params[6])
                w.type = 'INJ'
                continue
            if key == 'WELSPECS':
                if params[1] != '1*':
                    w.group = params[1]
                if params[2] != '1*':
                    w.x = params[2]
                if params[3] != '1*':
                    w.y = params[3]
                continue
            print(key + ' param left unread ')
        print(key + ' read done')


    def make_WELL(self, wname, x=1,y=1,z1=1,z2=1, phase='OIL', status = 'OPEN', skin = 0):
        """
        make new well keywords 
        adds new well's data into dict
        """
        l=[]
        if wname in self.wells:
            print('well with name '+ wname + ' already exist. command ignored')
            return l
        else:
            w = WellParam(wname)
            self.wells[wname] = w
        # store all data in dict
        w.x = x
        w.y = y 
        w.z1 = z1
        w.z2 = z2
        w.phase = phase
        w.status_perf = status 
        w.skin = skin
        # generate keywors       
        l.append('WELSPECS')
        s_welspecs_hints = ("-- WELLNAME GRPNAME I J BHPREF TYPE(PHASE) /" )
        s_welspecs = ("  " + wname + "     " + GROUP +
                 "   " + str(x) +
                 " " + str(y) +
                 " " + str(DEPTH) +
                 "        " + str(phase) + " /" )
        l.append(s_welspecs_hints)
        l.append(s_welspecs)
        l.append('/')
        l.append('COMPDAT')
        s_compdat_hints = ("-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /" )
        s_compdat = ("   " + wname + 
                 "   2*   " + str(z1) +
                 " " + str(z2) +
                 "  " + str(status) +
                 "     2*      " + str(DIAM) + 
                 "  1*  " + str(skin) + " /" )
        l.append(s_compdat_hints)
        l.append(s_compdat)   
        l.append('/')
        return l

    def make_perf(self, wname, z1_new, z2_new, status, skin=10):
        l = []
        if wname in self.wells:
            l.append('COMPDAT')
            s_compdat_hints = ("-- WELLNAME I J K1 K2 STATUS SATNUM  CF  RW(DIAM) KH SKIN  /" )
            s_compdat = ("   " + wname +
                         "   2*   " + str(z1_new) +
                         " " + str(z2_new) +
                         "  " + str(status) +
                         "     2*      " + "  1*  " +
                         "  1*  " + str(skin) + " /")
            l.append(s_compdat_hints)
            l.append(s_compdat)
            l.append('/')
        return l

    def make_WCONPROD(self, wname, qliq =10, bhp =50, status = 'OPEN', control = 'BHP', pump=0):
        """
        start stop production keyword
        pump - indicate pump type, 
               0 - self flow, 1 - 100-500, 2 -200-500, 3 - 200-1000
        """
        l=[]
        if wname in self.wells:
            w = self.wells[wname]
        else:
            print('well with name '+ wname + ' not found. command ignored')
            return l
            
        # store all data in dict
        w.lrat = qliq
        w.bhp = bhp 
        w.status_work = status
        w.control = control
        l.append('WCONPROD')
        s_wconprod_hints = ("-- WELLNAME STATUS ORATE CONTROL WRATE GRATE LRATE RESV BHP /" )
        s_wconprod = ("   " + wname + 
                      "    " + status +
                      "  " + control +
                      "           3*          " + str(qliq) +
                      "        1*   " + str(bhp) +
                      " /" )
        l.append(s_wconprod_hints)
        l.append(s_wconprod)
        l.append('/')
        return l
    
    def make_WCONINJE(self, wname, qliq =10, bhp =50, status = 'OPEN', control = 'BHP', pump=0):
        """
        start stop production keyword
        pump - indicate pump type, 
               0 - self flow, 1 - 100-500, 2 -200-500, 3 - 200-1000
        """
        l=[]
        if wname in self.wells:
            w = self.wells[wname]
        else:
            print('well with name '+ wname + ' not found. command ignored')
            return l

        w.lrat = qliq
        w.bhp = bhp
        w.status_work = status
        w.control = control
        l.append('WCONINJE')
        s_wconinje_hints = ("-- WELLNAME FLUID STATUS CONTROL RATE RESV BHP /" )
        s_wconinje = ("   " + wname + '   WATER '
                      " " + status +
                      "  " + control +
                      "     " + str(qliq) +
                      "        1*   " + str(bhp) +
                      " /")
        l.append(s_wconinje_hints)
        l.append(s_wconinje)
        l.append('/')
        return l
    
    def make_TSTEP(self, num = 1, step = 30):
        l =[]
        l.append('TSTEP')
        l.append(' ' + str(num)+'*'+str(step))
        l.append('/')
        return l

    def make_DATES(self, date):
        l =[]
        l.append('DATES')
        l.append(str(date) + '/')
        l.append('/')
        return l


class Events:
    """

    """
    def __init__(self, sname):
        self.excel = []
        self.sname = sname
        self.schedule = Schedule(sname)
        self.schedule_new = []
        self.time_step = 0
        self.year = 1

        

    def define_tstep_and_add_to_sch(self, tstep, step, year):
        if tstep == True:
            if year != self.year: 
                add_step = 365 - self.time_step
                self.schedule_new.extend(self.schedule.make_TSTEP(1, add_step))
                self.time_step = 0
                self.year += 1
            self.schedule_new.extend(self.schedule.make_TSTEP(1, step))
            self.time_step += step
                

    def change_GNO(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 3, year)
        wname = event['Название скважины']
        if wname in self.schedule.wells:
            if event['Тип насоса для установки'] == '':
                self.schedule.wells[wname].pump = ''
            else:
                self.schedule.wells[wname].pump = event['Тип насоса для установки']

    def zapusk(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 1, year)
        wname = event['Название скважины']
        if wname in self.schedule.wells:
            pump = self.schedule.wells[wname].pump
            if pump == '' or pump == 'Нет':
                pump = 'Насос 100-500'
            pump_rate = float(pump.split()[1].split('-')[0])
            pump_head = float(pump.split()[1].split('-')[1])
            pump_bhp_min = 250 - pump_head/10
            if not np.isnan(float(event['Контроль дебит/ Контроль закачка'])) and float(event['Контроль дебит/ Контроль закачка']) < pump_rate:
                qliq = float(event['Контроль дебит/ Контроль закачка'])
            else:
                qliq = pump_rate 
            if not np.isnan(float(event['Контроль Рзаб'])) and float(event['Контроль Рзаб']) > pump_bhp_min:
                bhp = float(event['Контроль Рзаб'])
            else:
                bhp = pump_bhp_min 
            status = 'OPEN'
            if self.schedule.wells[wname].type == 'PROD':
                if np.isnan(qliq):
                    control = 'BHP'
                    qliq = '1*'
                    if np.isnan(bhp):
                        bhp = 200
                elif np.isnan(bhp):
                    control = 'LRAT'
                    bhp = 200
                else:
                    control = 'BHP'
                self.schedule_new.extend(self.schedule.make_WCONPROD(wname, qliq, bhp, status, control))
            else:
                if not np.isnan(float(event['Контроль дебит/ Контроль закачка'])):
                    qliq = float(event['Контроль дебит/ Контроль закачка'])
                if not np.isnan(float(event['Контроль Рзаб'])):
                    bhp = float(event['Контроль Рзаб'])
                if np.isnan(qliq):
                    control = 'BHP'
                    qliq = '1*'
                    if np.isnan(bhp):
                        bhp = 400
                elif np.isnan(bhp):
                    control = 'RATE'
                    bhp = 400
                else:
                    control = 'BHP'
                self.schedule_new.extend(self.schedule.make_WCONINJE(wname, qliq, bhp, status, control))
        return

    def ostanovka(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 1, year)
        wname = event['Название скважины']
        if wname in self.schedule.wells:
            status = 'STOP'
            if self.schedule.wells[wname].type == 'PROD':
                self.schedule_new.extend(self.schedule.make_WCONPROD(wname, status = status))
            else:
                self.schedule_new.extend(self.schedule.make_WCONINJE(wname, status = status))
        return

    @staticmethod
    def determine_z(z_m):
        z_range = np.arange(2500, 2575, 5)
        i = 1
        for z in z_range:
            if int(z_m) > z:
                i += 1
            else:
                break
        return i

    def build_well(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 14, year)
        wname = event['Название скважины']
        if wname not in self.schedule.wells:
            x = int(event['координата i'])
            y = int(event['координата j'])
            if np.isnan(int(event['перфорация верх, м'])) or np.isnan(int(event['перфорация низ, м'])):
                z1 = 1
                z2 = 2
                status = 'SHUT'
            else:
                z1 = self.determine_z(int(event['перфорация верх, м']))
                z2 = self.determine_z(int(event['перфорация низ, м']))
                if z1 > 15:
                    z1 = 15
                if z2 > 15:
                    z2 = 15
                status = 'OPEN'
            z1 = min(z1, z2)
            z2 = max(z1, z2)
            if event['Тип скважины'] == 'Добывающая':
                phase = 'OIL'  # непонятно обязательно ли на нагн ставить воду т.к. это и отдельно при запуске задается
                w = WellParam(wname)
                w.type = 'PROD'
            else:
                phase = 'WATER'
                w = WellParam(wname)
                w.type = 'INJ'
            skin = 10
            self.schedule_new.extend(self.schedule.make_WELL(wname, x, y, z1, z2, phase, status, skin))
            self.schedule.wells[wname] = w
            self.change_GNO(event, tstep, year)
            self.zapusk(event, tstep, year)
            return

    def reperforation(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 4, year)
        wname = event['Название скважины']
        if wname in self.schedule.wells:
            z1_new = min(self.determine_z(event['перфорация верх, м']), self.determine_z(event['перфорация низ, м']))
            z2_new = max(self.determine_z(event['перфорация верх, м']), self.determine_z(event['перфорация низ, м']))
            if z2_new > 15: 
                z2_new = 15
            status = 'OPEN'
            self.schedule_new.extend(self.schedule.make_perf(wname, z1_new, z2_new,status))
        return
    
    def perevod(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 8, year)
        wname = event['Название скважины']
        if wname in self.schedule.wells:
            self.ostanovka(event, tstep, year)
            self.build_na_perev(event, tstep, year)
        return
    
    def build_na_perev(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 14, year)
        wname = event['Название скважины'] + '_perev'
        if wname not in self.schedule.wells:
            x = int(event['координата i'])
            y = int(event['координата j'])
            if np.isnan(int(event['перфорация верх, м'])) or np.isnan(int(event['перфорация низ, м'])):
                z1 = 1
                z2 = 2
                status = 'SHUT'
            else:
                z1 = self.determine_z(int(event['перфорация верх, м']))
                z2 = self.determine_z(int(event['перфорация низ, м']))
                if z1 > 15:
                    z1 = 15
                if z2 > 15:
                    z2 = 15
                status = 'OPEN'
            z1 = min(z1, z2)
            z2 = max(z1, z2)
            phase = 'WATER'
            w = WellParam(wname)
            w.type = 'INJ'
            skin = 10
            self.schedule_new.extend(self.schedule.make_WELL(wname, x, y, z1, z2, phase, status, skin))
            self.schedule.wells[wname] = w
            self.zapusk(event, tstep, year)
            return

    def OPZ(self, event, tstep, year):
        self.define_tstep_and_add_to_sch(tstep, 3, year)
        wname = event['Название скважины']
        if wname in self.schedule.wells:
            z1_new = ' 1* '
            z2_new = ' 1* '
            status = 'OPEN'
            skin = self.schedule.wells[wname].skin / 2
            self.schedule_new.extend(self.schedule.make_perf(wname, z1_new, z2_new, status, skin))
        return


    def read_excel(self, fname):
        excel = pd.read_excel(fname)
        excel.index.names = ['Index']
        excel.columns = list(excel.loc[6])
        excel = excel[excel.index > 6]
        excel = excel.loc[excel['Вид мероприятия'].isin(['Остановка скважины','Остановка скважины для КВД',
                                                        'Строительство новой скважины', 'Запуск скважины',
                                                                                   'Реперфорация', 'ОПЗ', 'Смена ГНО', 'Перевод в закачку'])]
        self.excel = excel
        for event in excel.iterrows():
            year = int(event[1]['Неделя'])
            tstep = True
            if event[1]['Вид мероприятия'] == 'Запуск скважины':
                self.zapusk(event[1], tstep, year)
            elif event[1]['Вид мероприятия'] == 'Остановка скважины' or event[1]['Вид мероприятия'] == 'Остановка скважины для КВД':
                self.ostanovka(event[1], tstep, year)
            elif event[1]['Вид мероприятия'] == 'Строительство новой скважины':
                self.build_well(event[1], tstep, year)
            elif event[1]['Вид мероприятия'] == 'Реперфорация':
                self.reperforation(event[1], tstep, year)
            elif event[1]['Вид мероприятия'] == 'ОПЗ':
                self.OPZ(event[1], tstep, year)
            elif event[1]['Вид мероприятия'] == 'Смена ГНО':
                self.change_GNO(event[1], tstep, year)
            elif event[1]['Вид мероприятия'] == 'Перевод в закачку':
                self.perevod(event[1], tstep, year)
                
                
        add_step = 365 - self.time_step
        self.schedule_new.extend(self.schedule.make_TSTEP(1, add_step))
        return


def make_initial_schedule(cname):
    l = []
    file1 = open('dataspace/rienm1_100x100x15_schedule.inc'.format(cname)).read()
    l.append(file1)
    with open("dataspace/{}/schedule_init_{}.inc".format(cname, cname), "w") as file:
        for item in l:
            print(item, file=file)
    return


def create_schedule_for_team(name):
    print("---Начало работы над созданием schedule секции для команды " + name + "---")
    make_initial_schedule(name)
    a = Events('dataspace/{}/schedule_init_{}.inc'.format(name, name))
    a.read_excel('dataspace/{}/Мероприятия РиЭНМ {}.xlsx'.format(name, name))
    l = []
    file = open('dataspace/{}/schedule_init_{}.inc'.format(name, name)).read()
    l.append(file)
    for a in a.schedule_new:
        l.append(a)
    with open("dataspace/{}/schedule_new_{}.inc".format(name, name), "w") as file:
        for item in l:
            print(item, file=file)

