# Q31. Write a program combining numpy, pandas, and matplotlib for simple data analysis.

# Import libraries
import numpy as np                  # NumPy → array operations
import pandas as pd                # Pandas → data handling (table form)
import matplotlib.pyplot as plt    # Matplotlib → graphs

# NumPy: create array of marks
marks = np.array([85, 90, 88, 75, 95])

# Pandas: create DataFrame (table)
df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": marks
})

# display data
print("Data:\n", df)

# Pandas Analysis
print("\nAverage Marks:", df["Marks"].mean())   # mean → average
print("Max Marks:", df["Marks"].max())          # max → highest value

# Matplotlib Visualization (Bar Graph)
plt.bar(df["Student"], df["Marks"])   # create bar graph
plt.title("Student Marks")            # graph title
plt.xlabel("Students")                # x-axis label
plt.ylabel("Marks")                   # y-axis label
plt.show()                            # display graph