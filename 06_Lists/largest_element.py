# Program to find the largest element in a list

# Create a list
numbers = [10, 45, 20, 80, 30]

# Assume the first element is the largest
largest = numbers[0]

# Check each element in the list
for num in numbers:
    if num > largest:
        largest = num

# Display the largest element
print("Largest element:", largest)