# Q29. Write a program using pandas to filter and group data.

import pandas as pd

# read csv file
df = pd.read_csv("data.csv")

print("Full Data:\n", df)

# Filtering (example: marks > 80)
filtered = df[df["marks"] > 80]
print("\nFiltered Data:\n", filtered)

# Grouping (example: by age)
grouped = df.groupby("age")["marks"].mean()
print("\nGrouped Data:\n", grouped)