# Q17. Write a program to read contents of a file using read(), readline(), and readlines().


# open file in read mode
file = open("sample.txt", "r")

# read() → reads full file
print("Using read():")
print(file.read())

file.close()


# reopen file
file = open("sample.txt", "r")

# readline() → reads one line at a time
print("\nUsing readline():")
print(file.readline())
print(file.readline())

file.close()


# reopen file
file = open("sample.txt", "r")

# readlines() → reads all lines as list
print("\nUsing readlines():")
lines = file.readlines()
print(lines)

file.close()