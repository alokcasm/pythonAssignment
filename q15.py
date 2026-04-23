# Q15. Write a program using built-in functions on list, string, and dictionary.

# List
a = [10, 20, 30, 40]

print("List:", a)
print("Length:", len(a))        # length of list
print("Max:", max(a))           # largest value
print("Min:", min(a))           # smallest value
print("Sum:", sum(a))           # total sum

# String
s = "alok"

print("\nString:", s)
print("Length:", len(s))        # length of string
print("Upper:", s.upper())      # uppercase
print("Lower:", s.lower())      # lowercase
print("Count of 'a':", s.count('a'))  # count character

# Dictionary
info = {
    "name": "Alok",
    "age": 20
}

print("\nDictionary:", info)
print("Length:", len(info))     # number of keys
print("Keys:", info.keys())     # all keys
print("Values:", info.values()) # all values