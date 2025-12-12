import joblib
import pandas as pd
import numpy as np
from config.config import MODEL_PATH
from schema.user_input import CarInput

class CarPriceModel:
    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        try:
            return joblib.load(MODEL_PATH)
        except FileNotFoundError:
            raise RuntimeError(f"Model not found at {MODEL_PATH}")

    def preprocess(self, input_data: CarInput) -> pd.DataFrame:
        """
        Converts Pydantic Input -> DataFrame with Feature Engineering.
        """
        # 1. Convert to Dict
        data = input_data.dict()
        df = pd.DataFrame([data])
        
        # 2. RENAME COLUMNS 
        df.rename(columns={
            'Model': 'Model_Grouped',          # Pipeline expects Model_Grouped
            'Gear_box_type': 'Gear box type',  # Pipeline expects spaces
            'Drive_wheels': 'Drive wheels',
            'Leather_interior': 'Leather interior',
            'Fuel_type': 'Fuel type'
        }, inplace=True)

        # 3. Feature Engineering
        current_year = 2025
        df['Age'] = current_year - df['Prod_year']
        
        # Avoid division by zero
        df['Km_per_Year'] = df['Mileage'] / (df['Age'] + 1)
        
        # Log Transforms
        df['Log_Levy'] = np.log1p(df['Levy'])
        df['Log_Mileage'] = np.log1p(df['Mileage'])
        
        # Turbo Logic
        df['Is_Turbo'] = 0

        return df

    def predict(self, input_data: CarInput) -> float:
        processed_df = self.preprocess(input_data)
        
        # Predict (Returns Log Price)
        log_price = self.model.predict(processed_df)[0]
        
        # Convert Log -> Real Price
        real_price = np.expm1(log_price)
        
        return round(real_price, 2)

# Create a singleton instance to be imported by app.py
model_service = CarPriceModel()