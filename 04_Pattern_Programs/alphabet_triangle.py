# Print an alphabet triangle

# Outer loop controls the rows
for i in range(1, 6):
    # Print alphabets from A to the row number
    for j in range(i):
        print(chr(65 + j), end=" ")

    print()