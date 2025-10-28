# Load raw datasets and initiate cleaning workflow
import pandas as pd
def load_data():
    sensor = pd.read_csv('data/raw/pump_sensor_data.csv')
    fabrics = pd.read_csv('data/raw/ten_fabrics_dataset.csv')
    industry = pd.read_csv('data/raw/faisalabad_textile_industries.csv')
    return sensor, fabrics, industry
