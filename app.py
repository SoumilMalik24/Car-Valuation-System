from fastapi import FastAPI, HTTPException
from schema.user_input import CarInput
from schema.prediction_response import PredictionResponse
from model.predict import model_service

app = FastAPI(title="CarValuator Enterprise API 🏎️")

@app.get("/")
def home():
    return {"health_check": "OK", "version": "1.0"}

@app.post("/predict", response_model=PredictionResponse)
def predict_price(car_details: CarInput):
    try:
        price = model_service.predict(car_details)
        return PredictionResponse(predicted_price=price)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))