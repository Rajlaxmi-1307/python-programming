# Program to remove duplicate elements from a list

# Create a list with duplicate values
numbers = [10, 20, 10, 30, 20, 40, 30]

# Create an empty list
new_list = []

# Check each element
for num in numbers:
    # Add only if the element is not already present
    if num not in new_list:
        new_list.append(num)

# Display both lists
print("Original list:", numbers)
print("List without duplicates:", new_list)