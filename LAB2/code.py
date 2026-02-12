import pandas as pd

# Load the dataset
df = pd.read_excel("data.xlsx")

# Display dataset shape
print("Dataset Shape (rows, columns):", df.shape)

# Preview first few rows
print("\nFirst 5 Rows:")
print(df.head())

# Display column names and data types
print("\nColumn Names and Data Types:")
print(df.dtypes)
