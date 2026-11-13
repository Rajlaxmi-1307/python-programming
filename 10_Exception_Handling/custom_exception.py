# Program to create a custom exception

# Define a custom exception class
class InvalidAgeError(Exception):
    pass


# Function to check voting eligibility
def check_age(age):

    # Check whether age is below 18
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    else:
        print("You are eligible to vote.")


try:
    # Take age input
    age = int(input("Enter your age: "))

    # Call the function
    check_age(age)

except ValueError:
    print("Error: Please enter a valid number.")

except InvalidAgeError as e:
    print("Custom Exception:", e)