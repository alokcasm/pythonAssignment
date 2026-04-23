# Q4. Write a program using if-else to find the largest of three numbers.

#Taking Input Of All Three Numbers...
a = int(input("Enter The Value Of a - "))
b = int(input("Enter The Value Of b - "))
c = int(input("Enter The Value Of c - "))


#Comparing a With b and c then b with a and c and we used else condition to find largest
if(a > b and a > c):
    print("a is largest number.")
elif(b > a and b > c):
    print("b is largest number.")
else:
    print("c is largest number.")
