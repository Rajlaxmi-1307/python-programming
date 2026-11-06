# Program to perform set operations

# Create two sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Display original sets
print("Set 1:", set1)
print("Set 2:", set2)

# Union - combines elements from both sets
print("Union:", set1.union(set2))

# Intersection - common elements
print("Intersection:", set1.intersection(set2))

# Difference - elements present in set1 but not set2
print("Difference:", set1.difference(set2))

# Symmetric difference - elements not common to both sets
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Add a new element
set1.add(70)
print("After adding 70:", set1)

# Remove an element
set1.remove(20)
print("After removing 20:", set1)