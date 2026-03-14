import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

# ---------- MODEL ----------
model = joblib.load("model.pkl")

# ---------- TITLE ----------
st.title("🏭 FactoryGuard AI")
st.subheader("Predictive Maintenance Intelligence Dashboard")

st.markdown("""
FactoryGuard AI is an AI-powered predictive maintenance system that analyzes
industrial machine sensor data to predict potential failures before they occur.

Predictive maintenance helps industries:

• Reduce downtime  
• Prevent machine breakdowns  
• Improve efficiency  
• Optimize maintenance planning
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

# ---------- PREDICTION ----------
features = np.array([[air_temp,process_temp,rpm,torque,wear,0,0,0,0,0,0]])

prediction = model.predict(features)

# ---------- HEALTH SCORE ----------
health = max(0,100-(wear*0.3 + torque*0.5))

st.header("Machine Health Score")

st.progress(int(health))

st.write("Health Score:", int(health), "%")

st.divider()

# ---------- FAILURE PROBABILITY ----------
failure_prob = min(1,(wear*0.01 + torque*0.01))

st.header("Failure Probability")

fig,ax = plt.subplots()

ax.bar(["Failure Risk"],[failure_prob],color="red")

ax.set_ylim(0,1)

st.pyplot(fig)

st.divider()

# ---------- SENSOR GRAPH ----------
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

This chart shows current machine sensor values.

Important indicators:

• High **Torque** increases mechanical stress  
• High **Tool Wear** indicates tool degradation  
• Abnormal values increase failure risk

The AI model analyzes these parameters to determine
machine health and predict possible failures.
""")

st.divider()

# ---------- AI RECOMMENDATION ----------
st.header("AI Recommendation")

if prediction[0]==1:

    st.error("⚠ Machine Failure Predicted")

    st.write("Recommended Actions:")

    st.write("- Inspect machine tool")
    st.write("- Reduce machine load")
    st.write("- Schedule maintenance")

else:

    st.success("✅ Machine Operating Normally")

    st.write("System Status: Stable")

st.divider()

# ---------- COST ----------
st.header("Maintenance Cost Estimate")

failure_cost = 5000
preventive_cost = 1500

if prediction[0]==1:

    st.write("Estimated breakdown cost:", failure_cost)

else:

    st.write("Estimated preventive maintenance cost:", preventive_cost)

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