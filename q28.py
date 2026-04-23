# Q28. Write a program using pandas to read a CSV file and perform basic analysis.


import pandas as pd

# read CSV file
df = pd.read_csv("data.csv")

# display data
print("Data:\n", df)

# basic analysis
print("\nFirst 5 rows:\n", df.head())
print("\nSummary:\n", df.describe())
print("\nColumn names:", df.columns)