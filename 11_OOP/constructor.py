# Program to demonstrate constructor

# Create a class
class Student:

    # Constructor
    def __init__(self, name, age, course):

        # Initialize object variables
        self.name = name
        self.age = age
        self.course = course

    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Course:", self.course)


# Create an object and pass values
student1 = Student("Rahul", 22, "MCA")

# Call display method
student1.display()