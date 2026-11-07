# Program to perform dictionary operations

# Create a dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "course": "MCA",
    "marks": 85
}

# Display the dictionary
print("Student Details:", student)

# Access dictionary values
print("Name:", student["name"])
print("Age:", student["age"])

# Add a new key-value pair
student["city"] = "Pune"
print("After adding city:", student)

# Update an existing value
student["marks"] = 90
print("After updating marks:", student)

# Remove a key-value pair
student.pop("age")
print("After removing age:", student)

# Display all keys and values
print("Dictionary Elements:")

for key, value in student.items():
    print(key, ":", value)