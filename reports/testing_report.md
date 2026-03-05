
# 1. Data Validation Testing

### Checks Performed:

- Missing value detection
- Duplicate record detection
- Data type validation
- Target variable validation

### Results:
- No missing values
- No duplicate records
- Proper data types confirmed

Dataset size: 10,000 × 14

Status:Passed

# 2. Class Distribution
### Machine Failure Distribution:

No Failure: 96.61%

Failure: 3.39%

### Observation:

Dataset is imbalanced.

Accuracy alone is not sufficient for evaluation.

### Mitigation:

Used class_weight='balanced'

Focused on Recall and F1-score

# 3. Model Testing

## 3. 1. Confusion Matrix
![alt text](image-1.png)

The confusion matrix shows how well the model predicted machine failures.


- 1961 machines were correctly predicted as No Failure

- 37 machines were correctly predicted as Failure

- 2 actual failures were missed

- 0 false alarms were generated

 <b>This means</b>

- The model did not give any wrong failure alert.

- It missed only 2 failures out of 39.

- This shows the model is highly reliable.

<b>In predictive maintenance:</b>

- Missing a failure is risky.

- Giving false alarms increases maintenance cost.

- Our model keeps both problems very low.

### 3.1.1 Accuracy

- Accuracy is 99.9%.

- This means almost all predictions are correct.

- But since the dataset is imbalanced (very few failures), we do not rely only on accuracy.

### 3.1.2 Precision

- Precision is 1.00 (100%).

- This means whenever the model predicts a failure, it is always correct.

- There are no unnecessary maintenance warnings.

- This is very important in industrial systems.

### 3.1.3 Recall

- Recall is about 94.87%.

- This means out of all actual failures, the model detected almost 95%.

- Only 2 failures were missed.

- This is considered strong performance in real-world predictive maintenance systems.

### 3.1.4 F1 Score

- F1 score is 0.97.

- F1 score balances precision and recall.

- Since both precision and recall are high, the F1 score is also strong.

- This confirms the model is well-balanced and stable.

## 3.2. ROC Curve (AUC = 0.9596)

- The ROC curve measures how well the model separates failure and non-failure cases.

- AUC score is 0.9596, which is very close to 1.

- This means there is a very high chance that the model correctly ranks failure cases higher than non-failure cases.
- In simple words the model can clearly distinguish between normal and faulty machines.

## 3.3. Precision-Recall Curve

- Since failures are rare (only 3.39%), this curve is very important.

- The curve shows:

       -Precision stays very high.

       -Recall also remains strong.

- This confirms the model performs well even for rare failure cases.

## 3.4. Random Forest Results
![alt text](image-2.png)

- Random Forest gave exactly the same results as Logistic Regression:

- Same confusion matrix

- Same precision, recall, and F1 score

- This shows:

        - The dataset is clean.

        - The features are strong.

        - The model is stable.

        - Results are not random.

# 4. Explainability Testing (SHAP Analysis)
## 4.1  Objective

- The objective of explainability testing was to ensure that the machine learning model:

- Makes logical and interpretable decisions

- Uses relevant features for prediction

- Does not behave like a black box

- Can justify why a machine is predicted as failure or non-failure

- In industrial predictive maintenance systems, explainability is important because maintenance actions involve cost, safety, and operational decisions.

## 4.2 Explainability Tool Used

- The SHAP (SHapley Additive Explanations) library was used for model interpretation.

- SHAP explains model predictions by assigning contribution values to each feature.
It shows how much each feature increases or decreases the probability of machine failure.

## 4.3 Implementation Process

- After training the Logistic Regression model, SHAP analysis was performed:

- Converted scaled training and testing data into DataFrame format

- Created SHAP Explainer object

- Generated SHAP values for test dataset

- Plotted global and local explanations

- Two types of explainability testing were performed:

      Global Explainability

      Local Explainability

## 4.4  Global Explainability Testing

- A SHAP bar plot was generated to show overall feature importance.

- Purpose: To identify which features have the highest impact on predicting machine failure.

- Observation: Operational parameters such as rotational speed, torque, tool wear, and temperature significantly influenced predictions.

- No irrelevant feature dominated the model decision.

- Validation Result: The model relies on logical mechanical and operational features.
This confirms that predictions are based on meaningful engineering parameters.

Status: Passed

## 4.5 Local Explainability Testing

- A SHAP waterfall plot was generated for individual machine predictions.

- Purpose: To explain why a specific machine was predicted as failure or non-failure.

- Interpretation:

      Positive SHAP value → Increases failure risk

      Negative SHAP value → Decreases failure risk

- Final prediction is the combined effect of all feature contributions

- Validation Result: Each prediction can be clearly explained.
There is no hidden or random decision-making.

Status: Passed
