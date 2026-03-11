import joblib
import numpy as np
import json

model = joblib.load("../model.pkl")

def handler(request):

    body = json.loads(request.body)

    air_temp = float(body["air_temp"])
    process_temp = float(body["process_temp"])
    rpm = float(body["rpm"])
    torque = float(body["torque"])
    wear = float(body["wear"])

    features = np.array([[air_temp, process_temp, rpm, torque, wear]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "⚠️ Machine Failure Predicted"
    else:
        result = "✅ Normal Machine Operation"

    return {
        "prediction": result
    }
