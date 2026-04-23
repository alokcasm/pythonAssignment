# Q8. Write a program using while loop to compute sum of first N natural numbers.

#taking input of a number
a = int(input("Enter A Number : "))

#initializing sum = 0 so that we can assign value after sum
sum = 0

for i in range (1,a+1): 
    sum += i #used for loop and we added all numbers one by one

print("Sum Of First",a,"Natural Numbers : ",sum)    #printing sum of first n natural number