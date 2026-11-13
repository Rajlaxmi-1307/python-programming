# Program to handle multiple exceptions

try:
    # Take input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform division
    result = num1 / num2

    print("Result:", result)

except ValueError:
    # Handle invalid input
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    # Handle division by zero
    print("Error: Cannot divide by zero.")

except Exception as e:
    # Handle any other unexpected exception
    print("Unexpected error:", e)

else:
    # Executes when no exception occurs
    print("Division completed successfully.")

finally:
    # Always executes
    print("Program execution finished.")