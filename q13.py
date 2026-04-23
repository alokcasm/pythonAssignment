# Q13. Write a program to perform tuple operations and demonstrate immutability.

# create tuple
t = (10, 20, 30, 40)

print("Original Tuple:", t)

# Access elements
print("First element:", t[0])
print("Last element:", t[-1])

# Slicing
print("Sliced tuple:", t[1:3])

# Length
print("Length of tuple:", len(t))

# Immutability (cannot change tuple)
# t[0] = 100   # This will give error

# Instead, create new tuple
t2 = t + (50,)
print("After adding element:", t2)