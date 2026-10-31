# Print a number pyramid

# Outer loop controls the rows
for i in range(1, 6):
    # Print spaces
    for j in range(5 - i):
        print(" ", end="")

    # Print numbers from 1 to the row number
    for j in range(1, i + 1):
        print(j, end="")

    # Print numbers in reverse order
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()