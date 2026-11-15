# Program to demonstrate inheritance

# Parent class
class Animal:

    def eat(self):
        print("Animal is eating.")


# Child class inherits Animal
class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


# Create an object of child class
dog1 = Dog()

# Call parent class method
dog1.eat()

# Call child class method
dog1.bark()