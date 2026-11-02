# Program to count vowels in a string

# Take string input from the user
text = input("Enter a string: ")

# Initialize vowel count
count = 0

# Check each character in the string
for ch in text:
    if ch.lower() in "aeiou":
        count = count + 1

# Display total vowels
print("Total vowels:", count)