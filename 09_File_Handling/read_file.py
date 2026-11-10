# Program to read data from a text file

# Open the file in read mode
file = open("E:\python-programming-practice.txt", "r")

# Read the complete file content
data = file.read()

# Display file content
print("File Content:")
print(data)

# Close the file
file.close()
