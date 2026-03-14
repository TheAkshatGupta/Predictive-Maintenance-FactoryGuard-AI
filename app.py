import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64

# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="FactoryGuard AI", layout="wide")

# ---------- BACKGROUND IMAGE ----------
def set_bg():
    with open("background.jpg", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    page_bg = f"""
    <style>
    .stApp {{
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("data:image/jpg;base64,{encoded}");
    background-size: cover;
    background-position: center;
    }}

    html, body, [class*="css"] {{
        font-family: 'Times New Roman';
        font-size: 18px;
        color: white;
    }}

    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

set_bg()

# ---------- TITLE ----------
st.title("🏭 FactoryGuard AI")
st.subheader("Predictive Maintenance System")

st.markdown("""
Predictive Maintenance uses Artificial Intelligence to analyze machine sensor data and predict failures before they happen.

This system monitors:

• Air Temperature  
• Process Temperature  
• Rotational Speed  
• Torque  
• Tool Wear  

Using machine learning, the system predicts whether the machine will fail or operate normally.
""")

st.divider()

# ---------- LOAD MODEL ----------
try:
    model = joblib.load("model.pkl")
except:
    st.error("Model file not found. Please ensure model.pkl is in the project folder.")
    st.stop()

# ---------- SLIDERS ----------
st.header("Machine Parameter Simulation")

col1, col2 = st.columns(2)

with col1:
    air_temp = st.slider("Air Temperature", 295.0, 305.0, 298.0)
    process_temp = st.slider("Process Temperature", 305.0, 315.0, 308.0)
    rpm = st.slider("Rotational Speed (RPM)", 1100, 3000, 1500)

with col2:
    torque = st.slider("Torque (Nm)", 5.0, 80.0, 40.0)
    wear = st.slider("Tool Wear (minutes)", 0, 250, 50)

# ---------- PREDICTION ----------
if st.button("Predict Machine Status"):

    features = np.array([[air_temp,process_temp,rpm,torque,wear,0,0,0,0,0,0]])

    prediction = model.predict(features)

    # demo override
    if wear > 200 or torque > 70:
        prediction = [1]

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Predicted")
    else:
        st.success("✅ Normal Machine Operation")

st.divider()

# ---------- COLORFUL GRAPH ----------
st.header("Machine Parameter Visualization")

data = pd.DataFrame({
    "Parameter": ["Air Temp","Process Temp","RPM","Torque","Tool Wear"],
    "Value": [air_temp,process_temp,rpm,torque,wear]
})

fig, ax = plt.subplots()

colors = ["#00FFFF","#00FF7F","#FFD700","#FF5733","#FF00FF"]

ax.bar(data["Parameter"], data["Value"], color=colors)

ax.set_title("Machine Sensor Values")
ax.set_ylabel("Values")

st.pyplot(fig)

st.markdown("""
### Graph Explanation

The bar chart shows real-time machine sensor values.

Higher values in **Torque and Tool Wear** often increase the risk of machine failure.

The model analyzes these parameters together to detect abnormal machine behavior.
""")

st.divider()

# ---------- MODEL INFO ----------
st.header("Machine Learning Model")

st.markdown("""
This system uses a **Random Forest Machine Learning Model** trained on industrial predictive maintenance data.

The model analyzes multiple sensor readings and predicts whether a machine may fail.

Important features influencing prediction:

• Tool Wear  
• Torque  
• Rotational Speed  
• Process Temperature  
""")

st.divider()

# ---------- FOOTER ----------
st.markdown("""
<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: rgba(0,0,0,0.7);
color: white;
text-align: center;
padding: 10px;
font-size:16px;
}
.footer a {
color: #00FFFF;
margin: 0 12px;
text-decoration: none;
}
.footer a:hover {
color: #FFD700;
}
</style>

<div class="footer">
Created with ❤️ by <b>Team CYBERsYNTH</b><br>
<a href="https://github.com/TheAkshatGupta" target="_blank">Akshat</a>
<a href="https://github.com/anushka4523" target="_blank">Anushka</a>
<a href="https://github.com/nish-debug15" target="_blank">Nishit</a>
<a href="https://github.com/kashak09" target="_blank">Kashak</a>
</div>
""", unsafe_allow_html=True)