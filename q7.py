# Q7. Write a program to iterate through string, list, and dictionary using loops.

# String
name = "alok"

# List
a = [10, 20, 30, 40]

# Dictionary
info = {
    "name": "Alok Kumar",
    "age": 20
}

# Iterating through string
print("String iteration:")
for ch in name:
    print(ch)

# Iterating through list
print("\nList iteration:")
for num in a:
    print(num)

# Iterating through dictionary (keys)
print("\nDictionary keys:")
for key in info:
    print(key)

# Iterating through dictionary (values)
print("\nDictionary values:")
for value in info.values():
    print(value)

# Iterating through dictionary (key + value)
print("\nDictionary key-value pairs:")
for key, value in info.items():
    print(key, ":", value)