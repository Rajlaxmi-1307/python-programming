# Print an inverted right triangle using stars

# Outer loop controls the rows
for i in range(5, 0, -1):
    # Inner loop prints stars
    for j in range(i):
        print("*", end=" ")
    print()