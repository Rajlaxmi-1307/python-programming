# Program to reverse a list

# Create a list
numbers = [10, 20, 30, 40, 50]

# Create an empty list
reverse_list = []

# Traverse the list from the last element
for i in range(len(numbers) - 1, -1, -1):
    reverse_list.append(numbers[i])

# Display original and reversed lists
print("Original list:", numbers)
print("Reversed list:", reverse_list)