# Q26. Write a program using finally and custom exceptions.

# custom exception + finally

class MyError(Exception):
    pass

try:
    num = int(input("Enter number: "))

    if num < 0:
        raise MyError("Negative not allowed")

    print("Number:", num)

except MyError as e:
    print(e)

finally:
    print("Done")