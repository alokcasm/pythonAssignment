# Q12. Write a program to demonstrate list slicing and list manipulation.


# list
nums = [10, 20, 30, 40, 50]

print("Original List:", nums)

# List Slicing
print("First 3 elements:", nums[0:3])
print("Last 2 elements:", nums[-2:])
print("Reversed List:", nums[::-1])

# List Manipulation

# Add element
nums.append(60)
print("After append:", nums)

# Insert element
nums.insert(1, 15)
print("After insert:", nums)

# Remove element
nums.remove(30)
print("After remove:", nums)

# Update element
nums[2] = 25
print("After update:", nums)