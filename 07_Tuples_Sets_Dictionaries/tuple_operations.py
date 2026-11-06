# Program to perform tuple operations

# Create a tuple
numbers = (10, 20, 30, 40, 50)

# Display the tuple
print("Original tuple:", numbers)

# Access tuple elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Find the length of the tuple
print("Length:", len(numbers))

# Count the occurrence of an element
print("Count of 20:", numbers.count(20))

# Find the index of an element
print("Index of 30:", numbers.index(30))

# Display tuple elements using a loop
print("Tuple elements:")

for num in numbers:
    print(num)
