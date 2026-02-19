import pandas as pd

df = pd.read_csv("data/ai4i_predictive_maintenance.csv")  
df = df.drop_duplicates()
df = df.dropna()
df.to_csv("data/cleaned_data.csv", index=False)
print("Cleaned dataset saved")
