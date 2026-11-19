# Program to create a custom iterator

# Create an iterator class
class MyNumbers:

    # Constructor
    def __init__(self):
        self.num = 1

    # Return iterator object
    def __iter__(self):
        return self

    # Return next value
    def __next__(self):

        if self.num <= 5:
            value = self.num
            self.num += 1
            return value

        else:
            raise StopIteration


# Create iterator object
numbers = MyNumbers()

# Display values
for num in numbers:
    print(num)