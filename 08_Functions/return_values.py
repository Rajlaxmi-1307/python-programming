# Program to return a value from a function

# Define a function
def multiply(a, b):
    result = a * b

    # Return the result
    return result

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Store the returned value
answer = multiply(num1, num2)

# Display the result
print("Multiplication:", answer)