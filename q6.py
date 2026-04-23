# Q6. Write a program using for loop to print multiplication table of a number.

#taking input of a number
a = int(input("Enter A Number : "))


#printing table of given number by user
print("======= Multiplication Table Of ",a,"=============")
for i in range(1,11): #used here for loop range 1 - 11 so that print upto 1 - 10
    print(a,"X",i,"=",a*i) 