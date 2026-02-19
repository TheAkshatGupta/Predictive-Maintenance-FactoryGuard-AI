# <u> Dataset Report  </u>
## actoryGuard AI- Predictive Maintenance Dataset Documentation

---

# 1. Introduction

This dataset represents industrial machine sensor readings collected for predictive maintenance analysis.  

The objective of this dataset is to enable early detection of machine failures by analyzing operational and environmental parameters.  

The dataset supports a **binary classification task**, where the model predicts whether a machine is likely to fail based on sensor measurements.

---

# 2. Dataset Summary

| Attribute | Description |
|------------|-------------|
| Domain | Industrial Manufacturing |
| Data Type | Structured Tabular Data |
| Learning Type | Supervised Classification |
| Target Variable | Machine failure |
| Total Records | 10,000 |
| Total Features | 14 Columns |
| Problem Type | Binary Classification |
| Data Format | CSV |

Cleaned dataset file: **[cleaned_data.csv](../data/cleaned_data.csv)**

---

# 3. Feature Description

Below is a detailed explanation of each feature in the dataset:

| Column Name | Description | Data Type | Category |
|--------------|------------|------------|------------|
| UDI | Unique record identifier | Integer | Identifier |
| Product ID | Product type identifier | Categorical | Metadata |
| Type | Product quality type (L, M, H) | Categorical | Machine Category |
| Air temperature [K] | Ambient air temperature | Float | Sensor |
| Process temperature [K] | Machine process temperature | Float | Sensor |
| Rotational speed [rpm] | Speed of machine rotation | Integer | Operational |
| Torque [Nm] | Applied torque load | Float | Operational |
| Tool wear [min] | Tool usage duration | Integer | Degradation |
| Machine failure | Target variable (0/1) | Binary | Target |
| TWF | Tool Wear Failure | Binary | Failure Indicator |
| HDF | Heat Dissipation Failure | Binary | Failure Indicator |
| PWF | Power Failure | Binary | Failure Indicator |
| OSF | Overstrain Failure | Binary | Failure Indicator |
| RNF | Random Failure | Binary | Failure Indicator |

---

# 4. Target Variable Explanation

### Machine failure

| Value | Meaning |
|--------|---------|
| 0 | No Failure |
| 1 | Failure Occurred |

This is the primary prediction target.

The additional failure columns (TWF, HDF, PWF, OSF, RNF) represent specific failure types that contribute to overall machine failure.

---

# 5. Dataset Characteristics

## 5.1 Class Imbalance

Machine failures are rare events compared to normal operation.

| Class | Nature |
|--------|---------|
| 0 (Normal) | Majority Class |
| 1 (Failure) | Minority Class |

This imbalance makes accuracy an unreliable metric.  
Therefore, Recall and F1-score are prioritized during model evaluation.

---

## 5.2 Time Dependency

Although explicit timestamps are not included, the dataset represents sequential machine operations.

A **time-based train-test split** is used to simulate real-world predictive scenarios and avoid data leakage.

---

## 5.3 Feature Distribution Behavior

Observations from EDA:

- Temperature features show clustered ranges.
- Torque and rotational speed demonstrate variation before failures.
- Tool wear increases progressively, indicating degradation trend.
- Certain failure types correlate strongly with temperature imbalance.

---

# 6. Data Preprocessing Summary

The following preprocessing steps were applied:

| Step | Action Taken | Purpose |
|------|--------------|----------|
| Missing Value Check | Verified no null values | Data consistency |
| Outlier Inspection | Checked sensor anomalies | Remove noise |
| Data Type Validation | Confirmed numerical integrity | Modeling readiness |
| Target Encoding | Verified binary encoding | Classification setup |
| Feature Scaling | Applied during modeling phase | Model stability |


---

# 7. Feature Categories

For modeling clarity, features are grouped as:

### 7.1 Sensor Features
- Air temperature
- Process temperature

### 7.2 Operational Features
- Rotational speed
- Torque

### 7.3 Degradation Feature
- Tool wear

### 7.4 Failure Indicators
- TWF
- HDF
- PWF
- OSF
- RNF

### 7.5 Target Variable
- Machine failure

---

# 8. Correlation Insights

Based on correlation analysis:

- Process temperature has moderate relationship with failure events.
- Torque variations correlate with overstrain failures.
- Tool wear strongly relates to tool wear failure.
- Certain failure indicators contribute directly to overall machine failure.

Multicollinearity was inspected to prevent unstable model behavior.

---

# 9. Modeling Implications

Based on dataset structure:

| Dataset Property | Modeling Decision |
|------------------|-------------------|
| Class imbalance | Use class_weight='balanced' |
| Numerical dominance | Apply feature scaling |
| Rare failures | Focus on Recall |
| Multiple failure types | Enable future multi-label extension |

---

# 10. Strengths of Dataset

+ Realistic industrial scenario  
+ Clear failure categorization  
+ Structured tabular format  
+ Suitable for explainable AI  
+ Clean and modeling-ready  

---


# 11. Conclusion

The dataset provides a structured and realistic foundation for predictive maintenance modeling.

Its combination of operational parameters, degradation indicators, and categorized failure types makes it well-suited for:

- Binary failure prediction
- Failure-type analysis
- Explainable AI integration (SHAP)
- Industrial decision-support systems

Proper handling of imbalance, validation strategy, and interpretability are critical to deriving reliable predictions.

This dataset serves as the backbone of the FactoryGuard AI predictive pipeline.

---



