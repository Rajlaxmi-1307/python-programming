# Program to find factorial using recursion

# Define a recursive function
def factorial(n):

    # Base condition
    if n == 0 or n == 1:
        return 1

    # Function calls itself
    else:
        return n * factorial(n - 1)


# Take input from the user
num = int(input("Enter a number: "))

# Check for negative input
if num < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Call the recursive function
    result = factorial(num)

    # Display the result
    print("Factorial:", result)
