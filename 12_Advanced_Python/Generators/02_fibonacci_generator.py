# Program to generate Fibonacci series using a generator

# Create generator function
def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):
        yield a

        # Update Fibonacci values
        a, b = b, a + b


# Take input from the user
n = int(input("Enter number of terms: "))

# Display Fibonacci series
print("Fibonacci Series:")

for num in fibonacci(n):
    print(num, end=" ")