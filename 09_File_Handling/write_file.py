# Program to write data into a text file

# Open the file in write mode
file = open("student.txt", "w")

# Write data into the file
file.write("Student Name: Rahul\n")
file.write("Course: MCA\n")
file.write("Subject: Python Programming\n")

# Close the file
file.close()

# Display success message
print("Data written successfully!")