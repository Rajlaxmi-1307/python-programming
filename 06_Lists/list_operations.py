# Program to perform different list operations

# Create a list
numbers = [10, 20, 30, 40]

print("Original list:", numbers)

# Add an element at the end
numbers.append(50)
print("After append:", numbers)

# Insert an element at index 2
numbers.insert(2, 25)
print("After insert:", numbers)

# Remove an element
numbers.remove(30)
print("After remove:", numbers)

# Delete an element using pop()
numbers.pop()
print("After pop:", numbers)

# Sort the list
numbers.sort()
print("After sorting:", numbers)

# Find the length
print("Length:", len(numbers))