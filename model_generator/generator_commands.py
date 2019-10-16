"""
@alexeyvodopyan
23.09

"""


class DataParser:
    """

    """
    def __init__(self, init_file, nx, ny, nz, dx, dy, dz, por, permx, permy, permz, prod_names, prod_xs,
                 prod_ys, prod_z1s, prod_z2s, inj_names, inj_xs, inj_ys, inj_z1s, inj_z2s):
        self.content = init_file.readlines()
        'Удалим переносы в конце строк'
        self.content = [line.rstrip('\n') for line in self.content]
        self.content = [line.strip() for line in self.content]
        self.dimens = None
        self.dx_dim = None
        self.dy_dim = None
        self.dz_dim = None
        self.tops_dim = None
        self.por_dim = None
        self.permx_dim = None
        self.permy_dim = None
        self.permz_dim = None
        self.welspecs = None
        self.compdat = None
        self.wconprod = None
        self.wconinje = None
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
        self.prod_names = prod_names
        self.prod_xs = prod_xs
        self.prod_ys = prod_ys
        self.prod_z1s = prod_z1s
        self.prod_z2s = prod_z2s
        self.inj_names = inj_names
        self.inj_xs = inj_xs
        self.inj_ys = inj_ys
        self.inj_z1s = inj_z1s
        self.inj_z2s = inj_z2s
        self.all_well_names = self.prod_names + self.inj_names
        self.all_well_xs = self.prod_xs + self.inj_xs
        self.all_well_ys = self.prod_ys + self.inj_ys
        self.all_well_z1s = self.prod_z1s + self.inj_z1s
        self.all_well_z2s = self.prod_z2s + self.inj_z2s
        self.all_well_fluid = ['OIL' for _ in range(len(self.prod_names))] + ['WAT' for _ in range(len(self.inj_names))]

    def parse_file(self, keyword):
        keyword_start_flag = False
        i = 0
        for line in self.content:
            if line[:2] == '--':  # comment in file detected
                i += 1
                continue
            elif keyword in line:
                keyword_start_flag = True
                print('%s detected' % keyword)
            elif keyword_start_flag and keyword == 'DIMENS':
                self.create_dimensions()
                self.content[i] = self.dimens
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'DX':
                self.create_dx_dim()
                self.content[i] = self.dx_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'DY':
                self.create_dy_dim()
                self.content[i] = self.dy_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'DZ':
                self.create_dz_dim()
                self.content[i] = self.dz_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'TOPS':
                self.create_tops()
                self.content[i] = self.tops_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'PORO':
                self.create_porosity()
                self.content[i] = self.por_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'PERMX':
                self.create_permx()
                self.content[i] = self.permx_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'PERMY':
                self.create_permy()
                self.content[i] = self.permy_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'PERMZ':
                self.create_permz()
                self.content[i] = self.permz_dim
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'WELSPECS':
                for prod, x, y, fluid in zip(self.all_well_names, self.all_well_xs,
                                             self.all_well_ys, self.all_well_fluid):
                    self.create_welspecs(prod, x, y, fluid)
                    self.content.insert(i, self.welspecs)
                    i += 1
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'COMPDAT':
                for well, x, y, z1, z2 in zip(self.all_well_names, self.all_well_xs, self.all_well_ys,
                                              self.all_well_z1s, self.all_well_z2s):
                    self.create_compdat(well, x, y, z1, z2)
                    self.content.insert(i, self.compdat)
                    i += 1
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'WCONPROD':
                for prod in self.prod_names:
                    self.create_wconprod(prod)
                    self.content.insert(i, self.wconprod)
                    i += 1
                keyword_start_flag = self.keyword_read(keyword)
            elif keyword_start_flag and keyword == 'WCONINJE':
                for inj in self.inj_names:
                    self.create_wconinje(inj)
                    self.content.insert(i, self.wconinje)
                    i += 1
                keyword_start_flag = self.keyword_read(keyword)
            i += 1

    @staticmethod
    def keyword_read(keyword):
        print('%s written' % keyword)
        keyword_start_flag = False
        return keyword_start_flag

    def create_tops(self):
        self.tops_dim = str(self.nx*self.ny) + '*8325 /'  # later we can change this depth, so now is constant

    def create_dimensions(self):
        self.dimens = str(self.nx) + ' ' + str(self.ny) + ' ' + str(self.nz) + ' /'
        return

    def create_dx_dim(self):
        self.dx_dim = str(self.nx*self.ny*self.nz) + '*' + str(self.dx) + ' /'

    def create_dy_dim(self):
        self.dy_dim = str(self.nx*self.ny*self.nz) + '*' + str(self.dy) + ' /'

    def create_dz_dim(self):
        self.dz_dim = str(self.nx*self.ny*self.nz) + '*' + str(self.dz) + ' /'

    def create_porosity(self):
        self.por_dim = str(self.nx*self.ny*self.nz) + '*' + str(self.por) + ' /'

    def create_permx(self):
        self.permx_dim = str(self.nx*self.ny*self.nz) + '*' + str(self.permx) + ' /'

    def create_permy(self):
        self.permy_dim = str(self.nx*self.ny*self.nz) + '*' + str(self.permy) + ' /'

    def create_permz(self):
        self.permz_dim = str(self.nx*self.ny*self.nz) + '*' + str(self.permz) + ' /'

    def create_welspecs(self, name, x, y, fluid):
        self.welspecs = name + ' G1 ' + str(x) + ' ' + str(y) + ' 8400 ' + fluid + ' /'

    def create_compdat(self, name, x, y, z1, z2):
        self.compdat = name + ' ' + str(x) + ' ' + str(y) + ' ' + str(z1) + ' ' + str(z2) + ' OPEN	1*	1*	0.5 /'

    def create_wconprod(self, name):
        self.wconprod = name + ' OPEN ORAT 20000 4* 1000 /'

    def create_wconinje(self, name):
        self.wconinje = name + ' WAT OPEN RATE 100000 1* 9014 /'
