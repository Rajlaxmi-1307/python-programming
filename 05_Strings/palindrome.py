# Program to check whether a string is palindrome

# Take string input from the user
text = input("Enter a string: ")

# Convert string to lowercase
text = text.lower()

# Reverse the string
reverse = text[::-1]

# Check whether original and reversed strings are equal
if text == reverse:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")