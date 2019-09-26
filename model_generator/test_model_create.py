from model_generator.model_create import ModelGenerator

model_factory = ModelGenerator(init_file_name='RIENM1_INIT.DATA', nx=20, ny=20, nz=5, dx=5, dy=5, dz=5, por=0.2,
                               permx=100, permy=100, permz=100, prod_names=['Well1', 'Well2', 'Well3', 'Well4'],
                               prod_xs=[1, 1, 10, 10], prod_ys=[10, 1, 10, 1], prod_z1s=[1, 1, 1, 1],
                               prod_z2s=[3, 3, 3, 3])
model_factory.create_lazy_5_spot()
