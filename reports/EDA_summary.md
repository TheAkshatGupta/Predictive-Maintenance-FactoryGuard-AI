#  Exploratory Data Analysis (EDA) Report  
## Predictive Maintenance – FactoryGuard AI  

---

## 1. Introduction

This Exploratory Data Analysis (EDA) report presents a detailed statistical and visual examination of the cleaned dataset (`cleaned_data.csv`) used in the FactoryGuard AI Predictive Maintenance project.

The objective of this analysis is to:

- Understand dataset structure and quality  
- Analyze feature distributions  
- Examine target imbalance  
- Identify relationships between operational parameters and machine failures  
- Derive insights for model development  

---

## 2. Dataset Overview

The dataset consists of operational machine sensor readings and failure indicators collected in an industrial environment.

### Dataset Dimensions

| Metric | Value |
|--------|--------|
| Total Records | 10,000 |
| Total Features | 14 |
| Numerical Features | 12 |
| Categorical Features | 2 |
| Missing Values | 0 |
| Duplicate Rows | 0 |
| Memory Usage | ~1.1 MB |

The dataset is clean, complete, and free from inconsistencies.

---

## 3. Feature Description

### 3.1 Input Features

| Feature | Type | Description |
|----------|------|------------|
| UDI | Integer | Unique Data Identifier |
| Product ID | Object | Unique product reference |
| Type | Categorical | Product quality type (L, M, H) |
| Air temperature [K] | Float | Ambient air temperature |
| Process temperature [K] | Float | Internal process temperature |
| Rotational speed [rpm] | Integer | Machine rotational speed |
| Torque [Nm] | Float | Applied torque |
| Tool wear [min] | Integer | Tool usage duration |

### 3.2 Target Variable

| Feature | Type | Description |
|----------|------|------------|
| Machine failure | Binary | 0 = No Failure, 1 = Failure |

### 3.3 Failure Type Indicators

| Indicator | Description |
|------------|------------|
| TWF | Tool Wear Failure |
| HDF | Heat Dissipation Failure |
| PWF | Power Failure |
| OSF | Overstrain Failure |
| RNF | Random Failure |

These indicators enable root-cause classification and improve interpretability.

---


## 4. Data Quality Assessment

-  No missing values  
-  No duplicate rows  
-  Consistent data types  
-  Clean and structured dataset  

The dataset is fully prepared for modeling without additional preprocessing.

## 5. Target Variable Distribution

| Class | Percentage |
|--------|------------|
| No Failure | 96.61% |
| Failure | 3.39% |

### Observation

The dataset is **highly imbalanced**, with failure cases representing only 3.39% of total records.

### Modeling Implication

- Accuracy alone is insufficient  
- Precision, Recall, F1-score, and ROC/PR curves are required  
- Class imbalance handling is necessary  

This justifies the use of `class_weight='balanced'` in the baseline model.

---

## 6. Key Insights from EDA

### 1. Temperature Features
- Air and Process temperature are strongly correlated.
- Process temperature is consistently higher than air temperature.

### 2. Tool Wear
- Tool wear shows a positive relationship with machine failure.
- Higher wear increases failure probability.

### 3. Torque
- Higher torque values are associated with mechanical stress.
- Positive correlation observed with machine failure.

### 4. Rotational Speed
- Mild negative relationship with failure.
- Most machines operate within a stable RPM range.

---

## 7.  Correlation Highlights

- Strong positive correlation between Air and Process temperature  
- Positive correlation between Tool Wear and Failure  
- Positive correlation between Torque and Failure  
- Moderate negative correlation between Rotational Speed and Torque  

---

## 8. Industrial Insights

- Machine failures are rare but critical events.
- Mechanical stress indicators are strong predictors.
- Temperature stability plays a significant role in machine reliability.
- The dataset reflects realistic industrial predictive maintenance conditions.

---

## 9. Modeling Considerations

Based on the EDA findings:

- Use stratified train-test split  
- Apply feature scaling where necessary  
- Handle class imbalance using:
  - SMOTE
  - Class weighting
  - Balanced ensemble methods  

### Recommended Models

- Logistic Regression  
- Random Forest  
- Gradient Boosting  
- XGBoost  


## 10. Conclusion

The exploratory analysis confirms that:

- The dataset is clean, consistent, and free from data quality issues.
- Machine failure events are rare, resulting in significant class imbalance.
- Tool wear and torque are the most influential predictive features associated with machine failure.
- The dataset provides a reliable foundation for developing a robust predictive maintenance model.
