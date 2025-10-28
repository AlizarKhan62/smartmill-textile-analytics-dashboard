# Run full cleaning pipeline
from src.data.make_dataset import load_data
from src.data.preprocess import clean_sensor_data
from src.data.load_data import clean_fabric_data
from src.data.merge_datasets import merge

sensor, fabrics, industry = load_data()
sensor = clean_sensor_data(sensor)
fabrics = clean_fabric_data(fabrics)
merged = merge(sensor, fabrics, industry)
print('✅ Data cleaned and merged successfully!')
