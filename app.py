import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import base64

st.set_page_config(page_title="FactoryGuard AI", layout="wide")

# ---------- BACKGROUND ----------
def set_bg():
    with open("background.jpg","rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

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

# ---------- LOAD MODEL ----------
model = joblib.load("model.pkl")

# ---------- TITLE ----------
st.title("🏭 FactoryGuard AI")
st.subheader("Predictive Maintenance Intelligence Dashboard")

st.markdown("""
FactoryGuard AI is an AI-powered predictive maintenance system that analyzes
industrial machine sensor data to detect potential failures before they occur.

Predictive maintenance helps industries:

• Reduce machine downtime  
• Prevent unexpected failures  
• Improve production efficiency  
• Optimize maintenance scheduling
""")

st.divider()

# ---------- SENSOR DASHBOARD ----------
st.header("Machine Sensor Dashboard")

c1,c2,c3,c4,c5 = st.columns(5)

air_temp = c1.slider("Air Temperature",295.0,305.0,298.0)
process_temp = c2.slider("Process Temperature",305.0,315.0,308.0)
rpm = c3.slider("RPM",1100,3000,1500)
torque = c4.slider("Torque",5.0,80.0,40.0)
wear = c5.slider("Tool Wear",0,250,50)

st.divider()

# ---------- MODEL PREDICTION ----------
features = np.array([[air_temp,process_temp,rpm,torque,wear,0,0,0,0,0,0]])

prediction = model.predict(features)

# ---------- MACHINE HEALTH ----------
health = max(0,100-(wear*0.3 + torque*0.5))

col1,col2 = st.columns(2)

# ---------- HEALTH GAUGE ----------
with col1:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health,
        title={'text': "Machine Health Score"},
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

# ---------- FAILURE PROBABILITY ----------
with col2:

    failure_prob = min(1,(wear*0.01 + torque*0.01))

    fig = go.Figure(go.Bar(
        x=["Failure Probability"],
        y=[failure_prob],
        marker_color="crimson"
    ))

    fig.update_layout(title="Failure Risk")

    st.plotly_chart(fig,use_container_width=True)

st.divider()

# ---------- SENSOR GRAPH + EXPLANATION ----------
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
### Sensor Analysis Explanation

This graph visualizes real-time machine sensor readings.

Key insights:

• **Torque** indicates mechanical load on the machine  
• **Tool Wear** shows the degradation of cutting tools  
• High values of both increase failure probability

Machine learning models analyze these parameters together
to predict whether a machine is likely to fail.
""")

st.divider()

# ---------- AI RECOMMENDATION ----------
st.header("AI Maintenance Recommendation")

if prediction[0]==1:

    st.error("⚠ Machine Failure Predicted")

    st.markdown("""
Recommended Actions:

• Inspect machine tool immediately  
• Reduce operational load  
• Schedule preventive maintenance  
• Monitor torque fluctuations
""")

else:

    st.success("✅ Machine Operating Normally")

    st.markdown("""
System Status:

• Machine health is stable  
• Continue routine monitoring  
• Schedule maintenance as per plan
""")

st.divider()

# ---------- COST ESTIMATION ----------
st.header("Maintenance Cost Estimation")

failure_cost = 5000
preventive_cost = 1500

if prediction[0]==1:

    st.write("Estimated breakdown cost:",failure_cost)

else:

    st.write("Estimated preventive maintenance cost:",preventive_cost)

st.divider()

# ---------- FOOTER ----------
st.markdown("""

---

Created with ❤️ by **Team CYBERsYNTH**

[Akshat](https://github.com/TheAkshatGupta) |
[Anushka](https://github.com/anushka4523) |
[Nishit](https://github.com/nish-debug15) |
[Kashak](https://github.com/kashak09)

""")
