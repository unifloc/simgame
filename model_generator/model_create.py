from model_generator.generator_commands import DataParser
import os
import ecl

"""
@alexeyvodopyan
23.09

"""


class ModelGenerator:
    """

    """

    def __init__(self, init_file_name='RIENM1_INIT.DATA', nx=20, ny=20, nz=5, dx=10, dy=10, dz=2, por=0.3, permx=100,
                 permy=100, permz=100, prod_names=None, prod_xs=None, prod_ys=None, prod_z1s=None, prod_z2s=None):
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
            prod_ys = [1, 3, 5]
        if prod_xs is None:
            prod_xs = [1, 3, 5]
        if prod_names is None:
            prod_names = ['PROD1', 'PROD2', 'PROD3']
        if prod_z1s is None:
            prod_z1s = [1, 1, 1]
        if prod_z2s is None:
            prod_z2s = [2, 2, 2]
        self.prod_names = prod_names
        self.prod_xs = prod_xs
        self.prod_ys = prod_ys
        self.prod_z1s = prod_z1s
        self.prod_z2s = prod_z2s
        self.init_file_name = init_file_name
        self.filter_initial_data()
        self.parser = None
        self.initialize_parser(self.init_file_name, self.nx, self.ny, self.nz, self.dx, self.dy, self.dz, self.por,
                               self.permx,
                               self.permy, self.permz, self.prod_names, self.prod_xs, self.prod_ys, self.prod_z1s,
                               self.prod_z2s)

    def initialize_parser(self, init_file_name, nx, ny, nz, dx, dy, dz, por, permx, permy, permz, prod_names, prod_xs,
                          prod_ys, prod_z1s, prod_z2s):
        init_file = open(init_file_name)
        self.parser = DataParser(init_file, nx, ny, nz, dx, dy, dz, por, permx, permy, permz, prod_names, prod_xs,
                                 prod_ys, prod_z1s, prod_z2s)

    def filter_initial_data(self):
        if max(self.prod_xs) > self.nx:
            print('Х-координата скважин больше Х-размерности модели. Проверьте свои данные')
        if max(self.prod_ys) > self.ny:
            print('Y-координата скважин больше Y-размерности модели. Проверьте свои данные')
        if max(self.prod_z2s) > self.nz:
            print('Z2-координата скважин больше Z-размерности модели. Проверьте свои данные')

    def create_5_spot(self):
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
        self.save_file(name='5_spot')
        self.calculate_file(name='5_spot')

    def create_lazy_5_spot(self):
        prod_xs = [1, 1, self.nx, self.nx]
        prod_ys = [1, self.ny, 1, self.ny]
        prod_z1s = [1, 1, 1, 1]
        prod_z2s = [self.nz, self.nz, self.nz, self.nz]
        self.initialize_parser(self.init_file_name, self.nx, self.ny, self.nz, self.dx, self.dy, self.dz, self.por,
                               self.permx,
                               self.permy, self.permz, self.prod_names, prod_xs, prod_ys, prod_z1s, prod_z2s)
        self.create_5_spot()

    def save_file(self, name='5_spot'):
        with open(name + '.DATA', "w") as file:
            for line in self.parser.content:
                print(line, file=file)

    @staticmethod
    def calculate_file(name='5_spot'):
        os.system("flow %s.DATA" % name)
