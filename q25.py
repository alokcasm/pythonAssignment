# Q25. Write a program demonstrating multiple exceptions handling.

# Multiple exception handling example (list + index)

try:
    lst = [10, 20, 30]

    index = int(input("Enter index: "))
    value = int(input("Enter value to divide: "))

    print("Element:", lst[index])
    print("Division result:", lst[index] / value)

except IndexError:
    print("Error: Index out of range")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

except Exception as e:
    print("Other error:", e)