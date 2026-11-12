# Program to create and read a CSV file

# Import the csv module
import csv

# Open CSV file in write mode
with open("students.csv", "w", newline="") as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["Roll No", "Name", "Marks"])

    # Write student records
    writer.writerow([1, "Rahul", 85])
    writer.writerow([2, "Amit", 90])
    writer.writerow([3, "Priya", 88])

# Display success message
print("CSV file created successfully!")

# Open CSV file in read mode
with open("students.csv", "r") as file:

    # Create a CSV reader object
    reader = csv.reader(file)

    # Display CSV data
    print("\nStudent Records:")

    for row in reader:
        print(row)