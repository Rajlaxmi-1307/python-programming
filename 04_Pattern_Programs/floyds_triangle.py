# Print Floyd's triangle

num = 1

# Outer loop controls the rows
for i in range(1, 6):
    # Print numbers in each row
    for j in range(i):
        print(num, end=" ")
        num = num + 1

    print()