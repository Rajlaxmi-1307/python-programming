# Program to demonstrate encapsulation

# Create a BankAccount class
class BankAccount:

    def __init__(self, balance):

        # Private variable
        self.__balance = balance

    # Method to deposit money
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Enter a valid amount.")

    # Method to display balance
    def display_balance(self):
        print("Account Balance:", self.__balance)


# Create an object
account = BankAccount(5000)

# Display initial balance
account.display_balance()

# Deposit money
account.deposit(2000)

# Display updated balance
account.display_balance()