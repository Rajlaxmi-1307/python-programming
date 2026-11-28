# Dequeue operation in Queue

queue = [10, 20, 30, 40]

# Check whether queue is empty
if len(queue) == 0:
    print("Queue is empty")
else:
    # Remove first element
    removed = queue.pop(0)

    print("Removed element:", removed)

# Display updated queue
print("Queue after Dequeue:", queue)
