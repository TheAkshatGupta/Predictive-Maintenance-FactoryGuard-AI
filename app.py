from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

class MachineData(BaseModel):
    air_temp: float
    process_temp: float
    rpm: float
    torque: float
    wear: float

@app.get("/")
def home():
    return {"message": "FactoryGuard AI API Running"}

@app.post("/predict")
def predict(data: MachineData):

    features = np.array([[

        data.air_temp,
        data.process_temp,
        data.rpm,
        data.torque,
        data.wear,
        0,0,0,0,0,0

    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "⚠️ Machine Failure Predicted"
    else:
        result = "✅ Normal Machine Operation"

    return {"prediction": result}
