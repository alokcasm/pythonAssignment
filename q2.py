# Q2. Write a program to perform all arithmetic operations on user input numbers.

#Taking Input Of Both Numbers
a = int(input("Enter Your First Number :- "))
b = int(input("Enter Your Second Number :- "))

#Performing Arithmetic Operations
sum = a + b
diff = a - b 
multi = a * b
div = a / b
modul = a % b 


#Printing All Arithmetic Result like after sum division substraction..
print("==========Arithmetic Operations Result===============")
print("Sum Of Your Both Number is ",sum)
print("Substraction Of Your Both Number is ",diff)
print("Multiplication Of Your Both Number is ",multi)
print("Division Of Your Both Number is ",div)
print("Remider When Your Both Number is Divided ",modul)
print("=================END===================================")