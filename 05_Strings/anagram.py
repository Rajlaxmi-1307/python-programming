# Program to check whether two strings are anagrams

# Take two string inputs
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Convert strings to lowercase and remove spaces
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Sort both strings
if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")