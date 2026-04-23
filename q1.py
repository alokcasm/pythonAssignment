# 1. Write a program to demonstrate different numeric data types(int, float) and type conversion.

a = 10        # int
b = 5.5       # float

# original values
print("Integer value (a):", a)
print("Float value (b):", b)

# Implicit type conversion (int to float)
sum_value = a + b
print("\nAfter implicit conversion (a + b):", sum_value)

# Explicit type conversion (float to int)
c = int(b)
print("After explicit conversion (float b to int):", c)

# Another example
x = 7
y = 2

# Without type casting (integer division not forced)
result1 = x / y
print("\nWithout type casting (x / y):", result1)

# With explicit type casting
result2 = int(x / y )
print("With type casting (float x / y):", result2)