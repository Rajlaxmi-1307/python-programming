# Pop operation in Stack

stack = [10, 20, 30, 40]

# Check whether stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    # Remove top element
    removed = stack.pop()

    print("Removed element:", removed)

# Display updated stack
print("Stack after Pop:", stack)