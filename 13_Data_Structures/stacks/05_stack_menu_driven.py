# Menu-driven Stack Program

stack = []

while True:
    print("\n--- Stack Operations ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        stack.append(value)
        print("Element inserted successfully")

    elif choice == 2:
        if not stack:
            print("Stack is empty")
        else:
            print("Removed:", stack.pop())

    elif choice == 3:
        if not stack:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        print("Stack:", stack)

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")