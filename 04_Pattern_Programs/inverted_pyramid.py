# Print an inverted pyramid using stars

# Outer loop controls the rows
for i in range(5, 0, -1):
    # Print spaces before stars
    for j in range(5 - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()