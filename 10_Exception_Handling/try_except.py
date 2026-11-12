# Program to handle an exception using try and except

# Take two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    # Perform division
    result = num1 / num2

    # Display result
    print("Division:", result)

except ZeroDivisionError:
    # Handle division by zero error
    print("Error: Cannot divide by zero.")

print("Program completed.")
