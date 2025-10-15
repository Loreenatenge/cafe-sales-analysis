import pandas as pd


df = pd.read_csv("dirty_cafe_sales.csv")
print("First 5 rows:")
print(df.head())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nData info:")
print(df.info())

# Checking the top 10 most purchased items
top_items = df['Item'].value_counts().head(10)
print("\nTop 10 Most Purchased Items:")
print(top_items)

