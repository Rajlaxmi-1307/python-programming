# Program to count the frequency of each word

# Take sentence input from the user
sentence = input("Enter a sentence: ")

# Convert the sentence into lowercase
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary
frequency = {}

# Count each word
for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1

    else:
        frequency[word] = 1

# Display word frequency
print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)