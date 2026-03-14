import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import shap
import base64
import time
import random

st.set_page_config(page_title="FactoryGuard AI", layout="wide")

# ---------------- BACKGROUND ----------------

def set_bg():
    with open("background.jpg","rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>

    .stApp {{
    background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
    url("data:image/png;base64,{encoded}");
    background-size: cover;
    }}

    html, body, [class*="css"] {{
    font-family: "Times New Roman";
    color: white;
    }}

    </style>
    """, unsafe_allow_html=True)

set_bg()

# ---------------- MODEL ----------------

model = joblib.load("model.pkl")

# ---------------- TITLE ----------------

st.title("🏭 FactoryGuard AI")
st.subheader("Enterprise Predictive Maintenance System")

st.markdown("""
FactoryGuard AI is an intelligent predictive maintenance platform designed
to monitor industrial machines using sensor data and machine learning.

Traditional maintenance systems rely on fixed schedules, which may either
cause unexpected failures or unnecessary servicing.

Predictive maintenance uses **AI and sensor analytics** to detect hidden
patterns in machine behaviour and predict failures before they occur.

This helps industries:

• Reduce downtime  
• Prevent costly breakdowns  
• Increase operational efficiency  
• Optimize maintenance planning
""")

st.divider()

# ---------------- SENSOR DASHBOARD ----------------

st.header("Machine Sensor Simulation")

col1,col2,col3,col4,col5 = st.columns(5)

air_temp = col1.slider("Air Temp",295.0,305.0,298.0)
process_temp = col2.slider("Process Temp",305.0,315.0,308.0)
rpm = col3.slider("RPM",1100,3000,1500)
torque = col4.slider("Torque",5.0,80.0,40.0)
wear = col5.slider("Tool Wear",0,250,50)

# ---------------- REAL TIME SIMULATION ----------------

st.subheader("Real-Time Sensor Simulation")

if st.button("Simulate Sensor Stream"):

    placeholder = st.empty()

    for i in range(10):

        simulated = {
            "Air Temp": air_temp + random.uniform(-1,1),
            "Process Temp": process_temp + random.uniform(-1,1),
            "RPM": rpm + random.randint(-100,100),
            "Torque": torque + random.uniform(-3,3),
            "Wear": wear + random.randint(-5,5)
        }

        placeholder.write(simulated)

        time.sleep(0.5)

st.divider()

# ---------------- PREDICTION ----------------

features = np.array([[air_temp,process_temp,rpm,torque,wear,0,0,0,0,0,0]])

prediction = model.predict(features)

# ---------------- HEALTH GAUGE ----------------

health = max(0,100-(wear*0.3 + torque*0.5))

col1,col2 = st.columns(2)

with col1:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health,
        title={'text': "Machine Health"},
        gauge={
            'axis':{'range':[0,100]},
            'bar':{'color':"cyan"},
            'steps':[
                {'range':[0,40],'color':'red'},
                {'range':[40,70],'color':'orange'},
                {'range':[70,100],'color':'green'}
            ]
        }
    ))

    st.plotly_chart(gauge,use_container_width=True)

# ---------------- FAILURE PROBABILITY ----------------

with col2:

    prob = min(1,(wear*0.01 + torque*0.01))

    fig = go.Figure(go.Bar(
        x=["Failure Probability"],
        y=[prob],
        marker_color="crimson"
    ))

    fig.update_layout(title="Failure Risk")

    st.plotly_chart(fig,use_container_width=True)

st.divider()

# ---------------- SENSOR GRAPH + EXPLANATION ----------------

col1,col2 = st.columns([1.5,1])

data = pd.DataFrame({
"Parameter":["Air Temp","Process Temp","RPM","Torque","Wear"],
"Value":[air_temp,process_temp,rpm,torque,wear]
})

with col1:

    fig,ax = plt.subplots()

    colors = ["cyan","lime","gold","orange","magenta"]

    ax.bar(data["Parameter"],data["Value"],color=colors)

    ax.set_title("Machine Sensor Visualization")

    st.pyplot(fig)

with col2:

    st.markdown("""
### Graph Explanation

This visualization shows real-time machine sensor values.

Key insights:

• High **Torque** increases mechanical stress  
• High **Tool Wear** indicates tool degradation  
• Abnormal sensor combinations increase failure probability  

Predictive maintenance models continuously analyze these signals
to detect early warning signs of machine failure.
""")

st.divider()

# ---------------- SHAP EXPLAINABLE AI ----------------

st.header("Explainable AI – Feature Importance")

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(features)

fig = plt.figure()

shap.summary_plot(shap_values,features,show=False)

st.pyplot(fig)

st.divider()

# ---------------- FAILURE TIMELINE ----------------

st.header("Predicted Failure Timeline")

timeline = pd.DataFrame({
"Time":["Now","1 Day","3 Days","1 Week"],
"Failure Risk":[prob,prob+0.1,prob+0.2,prob+0.3]
})

st.line_chart(timeline.set_index("Time"))

st.divider()

# ---------------- COST PREDICTION ----------------

st.header("Maintenance Cost Prediction")

failure_cost = 5000
preventive_cost = 1500

if prediction[0]==1:

    st.error("⚠ Machine Failure Predicted")

    st.write("Estimated Failure Cost:",failure_cost)

else:

    st.success("Machine Operating Normally")

    st.write("Estimated Preventive Maintenance Cost:",preventive_cost)

st.divider()

# ---------------- FOOTER ----------------

st.markdown("""

---

Created with ❤️ by **Team CYBERsYNTH**

[Akshat](https://github.com/TheAkshatGupta) |
[Anushka](https://github.com/anushka4523) |
[Nishit](https://github.com/nish-debug15) |
[Kashak](https://github.com/kashak09)

""")
