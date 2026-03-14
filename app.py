import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="FactoryGuard AI", layout="wide")

st.title("⚙️ FactoryGuard AI")
st.subheader("Predictive Maintenance System")

st.write(
"This system predicts whether a machine is likely to fail based on sensor readings."
)

model = joblib.load("model.pkl")

st.sidebar.header("Enter Machine Sensor Values")

UDI = st.sidebar.number_input("UDI", value=5000.0)

air_temp = st.sidebar.number_input("Air temperature [K]", value=300.0)
process_temp = st.sidebar.number_input("Process temperature [K]", value=310.0)
rpm = st.sidebar.number_input("Rotational speed [rpm]", value=1500.0)
torque = st.sidebar.number_input("Torque [Nm]", value=40.0)
tool_wear = st.sidebar.number_input("Tool wear [min]", value=100.0)

TWF = 0
HDF = 0
PWF = 0
OSF = 0
RNF = 0

input_df = pd.DataFrame({
    "UDI":[UDI],
    "Air temperature [K]":[air_temp],
    "Process temperature [K]":[process_temp],
    "Rotational speed [rpm]":[rpm],
    "Torque [Nm]":[torque],
    "Tool wear [min]":[tool_wear],
    "TWF":[TWF],
    "HDF":[HDF],
    "PWF":[PWF],
    "OSF":[OSF],
    "RNF":[RNF]
})

if st.button("Predict Machine Failure"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error("⚠️ Machine Failure Likely")
    else:
        st.success("✅ Machine Operating Normally")

    st.metric("Failure Probability", f"{probability:.2f}")

    st.subheader("Prediction Confidence")

    fig, ax = plt.subplots()

    labels = ["No Failure", "Failure"]
    values = [1 - probability, probability]

    ax.bar(labels, values)
    ax.set_ylabel("Probability")
    ax.set_title("Model Prediction Confidence")

    st.pyplot(fig)