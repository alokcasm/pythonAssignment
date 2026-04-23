# Q5. Write a program using nested if to classify a number (positive,negative, zero).

#taking input of a number by user
a = int(input("Enter A Number : "))

#nested if-else
if(a >= 0): #checking a is grater than and equal to 0 or not ?
    if(a == 0): #if a == 0
        print("Your Entered Number Is Zero.")
    else:
        print("Your Entered Number Is Positive.") #else a is positive
else:
    print("Your Entered Number Is Negative.") #used else cond. for checking negative number