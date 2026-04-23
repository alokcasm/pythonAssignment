# Q16. Write functions to organize a program that performs basic operations on strings and lists.

# Functions for string operations
def string_ops(s):
    print("Original String:", s)
    print("Length:", len(s))
    print("Upper:", s.upper())
    print("Reversed:", s[::-1])

# Functions for list operations
def list_ops(lst):
    print("\nOriginal List:", lst)
    print("Length:", len(lst))
    print("Max:", max(lst))
    print("Min:", min(lst))

    lst.append(100)
    print("After append:", lst)


# Main program
s = "alok"
lst = [10, 20, 30]

string_ops(s)
list_ops(lst)