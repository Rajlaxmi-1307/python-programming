# Program to demonstrate a simple decorator

# Create a decorator function
def my_decorator(func):

    # Create an inner function
    def wrapper():
        print("Before function execution")

        # Call the original function
        func()

        print("After function execution")

    return wrapper


# Apply decorator
@my_decorator
def greet():
    print("Hello! Welcome to Python.")


# Call the decorated function
greet()