# Program to demonstrate an iterator

# Create a list
numbers = [10, 20, 30, 40, 50]

# Convert list into an iterator
result = iter(numbers)

# Access elements one by one
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))