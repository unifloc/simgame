from model_generator.generator_commands import DataParser
import os
from ecl.summary import EclSum
import pandas as pd
import numpy as np
import plotly.graph_objects as go


"""
@alexeyvodopyan
23.09

"""

# TODO надо понять почему симулятор ругается когда я делаю nz=2


class ModelGenerator:
    """

    """

    def __init__(self, init_file_name='RIENM1_INIT.DATA', nx=100, ny=100, nz=3, dx=500, dy=500, dz=20, por=0.3, permx=100,
                 permy=100, permz=100, prod_names=None, prod_xs=None, prod_ys=None, prod_z1s=None, prod_z2s=None,
                 inj_names=None, inj_xs=None, inj_ys=None, inj_z1s=None, inj_z2s=None):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.por = por
        self.permx = permx
        self.permy = permy
        self.permz = permz

        if prod_ys is None:
            prod_ys = [1, 3, 5, 7]
        if prod_xs is None:
            prod_xs = [1, 3, 5, 7]
        if prod_names is None:
            prod_names = ['PROD1', 'PROD2', 'PROD3', 'PROD4']
        if prod_z1s is None:
            prod_z1s = [1, 1, 1, 1]
        if prod_z2s is None:
            prod_z2s = [2, 2, 2, 2]
        if inj_ys is None:
            inj_ys = [1]
        if inj_xs is None:
            inj_xs = [7]
        if inj_names is None:
            inj_names = ['INJ1']
        if inj_z1s is None:
            inj_z1s = [1]
        if inj_z2s is None:
            inj_z2s = [2]

        self.prod_names = prod_names
        self.prod_xs = prod_xs
        self.prod_ys = prod_ys
        self.prod_z1s = prod_z1s
        self.prod_z2s = prod_z2s
        self.inj_ys = inj_ys
        self.inj_xs = inj_xs
        self.inj_names = inj_names
        self.inj_z1s = inj_z1s
        self.inj_z2s = inj_z2s
        self.result_df = None
        self.fig = None
        self.init_file_name = init_file_name
        self.filter_initial_data()
        self.parser = None
        self.initialize_parser(self.init_file_name, self.nx, self.ny, self.nz, self.dx, self.dy, self.dz, self.por,
                               self.permx, self.permy, self.permz, self.prod_names, self.prod_xs, self.prod_ys,
                               self.prod_z1s, self.prod_z2s, self.inj_names, self.inj_xs, self.inj_ys, self.inj_z1s,
                               self.inj_z2s)

    def initialize_parser(self, init_file_name, nx, ny, nz, dx, dy, dz, por, permx, permy, permz, prod_names, prod_xs,
                          prod_ys, prod_z1s, prod_z2s, inj_names, inj_xs, inj_ys, inj_z1s, inj_z2s):
        init_file = open(init_file_name)
        self.parser = DataParser(init_file, nx, ny, nz, dx, dy, dz, por, permx, permy, permz, prod_names, prod_xs,
                                 prod_ys, prod_z1s, prod_z2s, inj_names, inj_xs, inj_ys, inj_z1s, inj_z2s)

    def filter_initial_data(self):
        if max(self.prod_xs) > self.nx:
            print('Х-координата скважин больше Х-размерности модели. Проверьте свои данные')
        if max(self.prod_ys) > self.ny:
            print('Y-координата скважин больше Y-размерности модели. Проверьте свои данные')
        if max(self.prod_z2s) > self.nz:
            print('Z2-координата скважин больше Z-размерности модели. Проверьте свои данные')

    def create_model(self, name, result_name, keys):
        self.parser.parse_file('DIMENS')
        self.parser.parse_file('DX')
        self.parser.parse_file('DY')
        self.parser.parse_file('DZ')
        self.parser.parse_file('TOPS')
        self.parser.parse_file('PORO')
        self.parser.parse_file('PERMX')
        self.parser.parse_file('PERMY')
        self.parser.parse_file('PERMZ')
        self.parser.parse_file('WELSPECS')
        self.parser.parse_file('COMPDAT')
        self.parser.parse_file('WCONPROD')
        self.parser.parse_file('WCONINJE')
        self.save_file(name=name)
        self.calculate_file(name=name)
        self.create_result(name=name, keys=keys)
        self.read_result(name=result_name)
        self.make_plot()

    def create_lazy_5_spot(self):
        prod_xs = [1, 1, self.nx, self.nx]
        prod_ys = [1, self.ny, 1, self.ny]
        prod_z1s = [1, 1, 1, 1]
        prod_z2s = [self.nz, self.nz, self.nz, self.nz]
        inj_xs = [int(self.nx/2)]
        inj_ys = [int(self.ny/2)]
        inj_z1s = [1]
        inj_z2s = [self.nz]
        self.initialize_parser(self.init_file_name, self.nx, self.ny, self.nz, self.dx, self.dy, self.dz, self.por,
                               self.permx, self.permy, self.permz, self.prod_names, prod_xs, prod_ys, prod_z1s,
                               prod_z2s, self.inj_names, inj_xs, inj_ys, inj_z1s, inj_z2s)
        self.create_model(name='5_spot', result_name='5_spot_result', keys=["WOPR:*", "WWPR:*", "WLPR:*",
                                                                            "WGPR:*", "WWIR:*", "WGOR:*", "WBHP:*",
                                                                            "WOPT:*", "WWPT:*", "WLPT:*", "WGPT:*",
                                                                            "WWIT:*", "FOPT", "FWPT", "FLPT", "FGPT",
                                                                            "FWIT"])

    def save_file(self, name='5_spot'):
        with open(name + '.DATA', "w") as file:
            for line in self.parser.content:
                print(line, file=file)

    @staticmethod
    def calculate_file(name='5_spot'):
        os.system("flow %s.DATA" % name)

    @staticmethod
    def create_result(name='5_spot', keys=None):
        summary = EclSum('%s.DATA' % name)
        dates = summary.dates
        results = []
        all_keys = []

        if keys is None:
            keys = ["WOPR:*"]

        for key in keys:
            key_all_wells = summary.keys(key)
            all_keys = all_keys + list(key_all_wells)

        for key in all_keys:
            results.append(list(summary.numpy_vector(key)))

        if len(results) == 0:
            return print('Результаты из модели не загрузились. Файл с результатами не был создан')

        result_df = pd.DataFrame(data=np.array(results).T, index=dates, columns=all_keys)
        result_df.index.name = 'Time'
        result_df.to_csv('%s_result.csv' % name)
        print('%s_result.csv is created' % name)

    def read_result(self, name='5_spot_result'):
        self.result_df = pd.read_csv('%s.csv' % name, parse_dates=[0], index_col=[0])
        print('%s.csv is read' % name)

    def make_plot(self, df=None, parameters=None, mode='markers'):
        if df is None:
            df = self.result_df

        self.fig = go.Figure()

        if parameters is None:
            parameters = df.columns

        for par in parameters:
            self.fig.add_trace(go.Scatter(
                x=df.index,
                y=df[par],
                mode=mode,
                ))

        print('График построен и сохранен в атрибутах класса')
