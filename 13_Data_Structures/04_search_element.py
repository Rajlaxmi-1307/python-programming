# Search for an element in an array

arr = [10, 20, 30, 40, 50]

# Element to search
search = 30

# Check whether the element exists
if search in arr:
    print("Element found at index:", arr.index(search))
else:
    print("Element not found")