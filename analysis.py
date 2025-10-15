import pandas as pd

# Load your dataset
data = pd.read_csv("dirty_cafe_sales.csv")
# Preview the first few rows
print("First 5 rows:")
print(data.head())

# Check for missing values
print("\nMissing values per column:")
print(data.isnull().sum())

# Summary info
print("\nData info:")
print(data.info())
