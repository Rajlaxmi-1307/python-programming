# Program to demonstrate polymorphism

# Create a class for Dog
class Dog:

    def sound(self):
        print("Dog barks.")


# Create a class for Cat
class Cat:

    def sound(self):
        print("Cat meows.")


# Create objects
dog = Dog()
cat = Cat()

# Call the same method on different objects
dog.sound()
cat.sound()