import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="FactoryGuard AI", layout="centered")

st.title("FactoryGuard AI")
st.subheader("Predictive Maintenance System")

model = joblib.load("model.pkl")

st.write("Enter machine parameters:")

air_temp = st.slider("Air Temperature", 295.0, 305.0, 298.0)
process_temp = st.slider("Process Temperature", 305.0, 315.0, 308.0)
rpm = st.slider("Rotational Speed (RPM)", 1100, 3000, 1500)
torque = st.slider("Torque (Nm)", 5.0, 80.0, 40.0)
wear = st.slider("Tool Wear (min)", 0, 250, 50)

if st.button("Predict Machine Status"):

    features = np.array([[

        air_temp,
        process_temp,
        rpm,
        torque,
        wear,
        0,0,0,0,0,0

    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Predicted")
    else:
        st.success("✅ Normal Machine Operation")
