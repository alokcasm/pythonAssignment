# Q30. Write a program using matplotlib to plot line and bar graphs.

import matplotlib.pyplot as plt

# sample data
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# Line Graph
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Bar Graph
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()