# Q14. Write a program to perform dictionary operations (add, update, delete).


# created a dictionary
info = {
    "name": "Alok",
    "age": 20
}

print("Original Dictionary:", info)

# Added new key-value pair
info["city"] = "Patna"
print("After adding:", info)

# Updated value
info["age"] = 21
print("After updating:", info)

# Deleted element
del info["city"]
print("After deleting:", info)