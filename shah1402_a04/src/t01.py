"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""

# imports
from Queue_circular import Queue

queue = Queue()

Queue_capacity = 0
print("Inserting elements into the queue...")
for i in range(Queue_capacity):
    queue.insert(i)
    print(f"Inserted {i} into the queue.")

if queue.is_empty():
    print("The queue is empty.")
else:
    print("The queue is not empty.")

if queue.is_full():
    print("The queue is full.")
else:
    print("The queue is not full.")

if Queue_capacity > 0:
    first_element = queue.peek()
    print(f"The first element in the queue is: {first_element}")

    removed_element = queue.remove()
    print(f"Removed element {removed_element} from the queue.")

    print(f"The queue has {len(queue)} elements.")

    another_queue = Queue()
    for i in range(5):
        another_queue.insert(i)

    if queue == another_queue:
        print("The queues are equal.")
    else:
        print("The queues are not equal.")

    print("Iterating over the queue:")
    for value in queue:
        print(value)
