# Program to append data into a text file

# Open the file in append mode
file = open("student.txt", "a")

# Add new data at the end of the file
file.write("College: ABC College\n")
file.write("Year: Second Year\n")

# Close the file
file.close()

# Display success message
print("Data appended successfully!")