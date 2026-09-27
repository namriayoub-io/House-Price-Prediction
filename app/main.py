from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model/house_price_model.pkl")


@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}


class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.post("/predict")
def predict(data: HouseFeatures):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_price": float(prediction)
    }