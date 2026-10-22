age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Free")
elif age < 18:
    print("Ticket price: ₹100")
elif age < 60:
    print("Ticket price: ₹200")
else:
    print("Ticket price: ₹150")