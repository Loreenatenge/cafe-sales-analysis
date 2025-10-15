import pandas as pd

# Load your dataset
df = pd.read_csv("dirty_cafe_sales.csv")
# Preview the first few rows
print("First 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Summary info
print("\nData info:")
print(df.info())

# Check top 10 most purchased items
top_items = df['Item'].value_counts().head(10)
print("\nTop 10 Most Purchased Items:")
print(top_items)

