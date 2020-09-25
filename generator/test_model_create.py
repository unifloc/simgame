from model_generator.model_create import ModelGenerator
model_factory = ModelGenerator()
# model_factory.create_lazy_5_spot()
# model_factory.create_result(name='spe1')
model_factory.export_snapshots(name='5_SPOT')
