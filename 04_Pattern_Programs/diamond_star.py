# Print a diamond star pattern

# Upper half of the diamond
for i in range(1, 5):
    # Print spaces
    for j in range(4 - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Lower half of the diamond
for i in range(3, 0, -1):
    # Print spaces
    for j in range(4 - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()