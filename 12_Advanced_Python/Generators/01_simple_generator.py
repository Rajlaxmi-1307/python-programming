# Program to demonstrate a simple generator

# Create a generator function
def numbers():

    yield 10
    yield 20
    yield 30
    yield 40
    yield 50


# Call the generator
result = numbers()

# Display values using a loop
for num in result:
    print(num)