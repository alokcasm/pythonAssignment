# Q20. Write a program to demonstrate file pointer operations using seek().


file = open("sample.txt", "r")

# Read first 5 characters
print("First 5 characters:", file.read(5))

# Move pointer to beginning
file.seek(0)
print("After seek(0):", file.read(5))

# Move pointer to 6th position
file.seek(6)
print("From position 6:", file.read(5))

file.close()