# Program to create a decorator for a function with arguments

# Create decorator
def my_decorator(func):

    def wrapper(a, b):
        print("Addition operation started")

        # Call original function
        func(a, b)

        print("Addition operation completed")

    return wrapper


# Apply decorator
@my_decorator
def add(a, b):
    print("Addition:", a + b)


# Call function
add(10, 20)