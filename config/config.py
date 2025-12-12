import os

current_file_path = os.path.abspath(__file__)


config_dir = os.path.dirname(current_file_path)

BASE_DIR = os.path.dirname(config_dir)


MODEL_PATH = os.path.join(BASE_DIR, "model", "car_price_model.pkl")

