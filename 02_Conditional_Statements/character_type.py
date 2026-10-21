ch = input("Enter a character: ")

if len(ch) != 1:
    print("Enter exactly one character.")
elif ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")