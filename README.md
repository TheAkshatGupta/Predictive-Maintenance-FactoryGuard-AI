# Predictive Maintenance – FactoryGuard AI

## Project Overview
This project focuses on building an **industrial Predictive Maintenance system** to predict machine failures using sensor and operational data.  
The goal is to develop a **clean, explainable, and production-oriented ML pipeline** rather than only optimizing for accuracy.

---

## Problem Statement
Unexpected machine failures lead to downtime and high maintenance costs.  
Using historical machine data, we aim to **predict machine failure in advance** so that preventive actions can be taken.

---

## Dataset
- Predictive Maintenance (AI4I-style) dataset  
- Structured, tabular machine operating data  
- Target variable: **Machine failure (binary classification)**  

### Key Features
- Air temperature  
- Process temperature  
- Rotational speed  
- Torque  
- Tool wear  
- Failure indicators (TWF, HDF, PWF, OSF, RNF)

---

## Tech Stack
- **Python**
- **Pandas, NumPy** – Data processing  
- **Scikit-learn** – Modeling & evaluation  
- **Logistic Regression, Random Forest** – ML models  
- **SHAP** – Explainability  
- **GitHub** – Version control  

---

## Project Workflow
1. Data cleaning and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Baseline model development  
4. Improved model implementation  
5. Model evaluation  
6. Explainability using SHAP  
7. Documentation and review preparation  

---

## Models Implemented

### Baseline Model – Logistic Regression
- Time-based train–test split  
- Class imbalance handled using `class_weight='balanced'`  
- Evaluation metrics: **F1-score, Recall, Confusion Matrix**

### Improved Model – Random Forest
- Same data split and evaluation strategy as baseline  
- Captures non-linear relationships  
- Comparable performance, validating baseline stability  

---

## Model Comparison

| Model | F1 Score | Recall |
|------|----------|--------|
| Logistic Regression | Reported | Reported |
| Random Forest | Reported | Reported |

---

## Explainability (SHAP)
To ensure transparency and trust:
- **Global SHAP analysis** identifies the most influential features affecting machine failure.
- **Local SHAP explanations** show how individual features impact predictions for a specific machine instance.

---

## Key Takeaways
- Clean data can make simple models very effective  
- Explainability is crucial for industrial ML adoption  
- Focus was on pipeline correctness and interpretability  

---

## Future Improvements
- Hyperparameter tuning  
- Advanced ensemble models  
- Real-time deployment pipeline  

---

## Team
- **Akshat Gupta** – Team Lead, Data Processing & Explainability  
- **Nishit** – Modeling  
- **Kashak** – Documentation  
- **Anushka** – EDA & Analysis  

---

## Project Status

This project has been finalized at the notebook (research and experimentation) level.

The complete machine learning pipeline has been implemented using Jupyter notebooks,
including:
- Data cleaning and exploratory data analysis
- Baseline and improved model training
- Model evaluation using F1-score and recall
- Model explainability using SHAP

The focus of this project was on understanding and analyzing predictive maintenance
using real-world sensor data rather than deployment.
