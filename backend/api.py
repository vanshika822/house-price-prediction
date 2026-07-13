import pandas as pd
import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load Saved Model
model = joblib.load("house_model.pkl")


# Input Structure
class HouseInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    house_age: int
    distance_city: float
    parking: int
    floor: int


@app.get("/")
def home():
    return {"message": "FastAPI Working"}


@app.post("/predict")
def predict(data: HouseInput):

    features = np.array([[
        data.area,
        data.bedrooms,
        data.bathrooms,
        data.house_age,
        data.distance_city,
        data.parking,
        data.floor
    ]])

    prediction = model.predict(features)
    history = {
    "area": data.area,
    "bedrooms": data.bedrooms,
    "bathrooms": data.bathrooms,
    "house_age": data.house_age,
    "distance_city": data.distance_city,
    "parking": data.parking,
    "floor": data.floor,
    "predicted_price": round(float(prediction[0]),2)
}

    history_df = pd.DataFrame([history])

    file_name = "prediction_history.csv"

    if os.path.exists(file_name):
        history_df.to_csv(file_name, mode="a", header=False, index=False)
    else:
        history_df.to_csv(file_name, index=False)

    return {
            "predicted_price": round(float(prediction[0]), 2)
    }