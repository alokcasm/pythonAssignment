# Q19. Write a program to copy contents of one file to another.


# open source file in read mode
f1 = open("source.txt", "r")

# open destination file in write mode
f2 = open("dest.txt", "w")

# read data from source and write to destination
data = f1.read()
f2.write(data)

# close files
f1.close()
f2.close()

print("File copied successfully")