# Q3. Write a program to demonstrate variable assignment and swapping values.


#Taking Input Of Both Value Of a And b
a = int(input("Enter The Value Of a - "))
b = int(input("Enter The Value Of b - "))


#Printing Both Values Before Swapping
print("===============Before Swapping=================")
print("a =",a)
print("b =",b)


#Swapping Both Values of a And b With Help Of temp Variable.
temp = b
b = a
a = temp


#Printing Value After SWapping Both Variable a And b
print("===============After Swapping=================")
print("a =",a)
print("b =",b)