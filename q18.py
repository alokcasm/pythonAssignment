# Q18. Write a program to write and append data to a file.


# Write mode (creates new file / overwrites old data)
file = open("sample2.txt", "w")
file.write("Hello !!\n")
file.write("Welcome to Python\n")
file.close()

print("Data written successfully")

# Append mode (adds data at end of file)
file = open("sample2.txt", "a")
file.write("This is appended line\n")
file.close()

print("Data appended successfully")