"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports

from Queue_circular import Queue

queue1 = Queue()
queue2 = Queue()


numbers = [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, ]


# Insert the same elements into both queues
for element in numbers:
    queue1.insert(element)
    queue2.insert(element)
print("Queue 1:")
for q in queue1:  # Queue1 contents
    print(q)
print("Queue 2:")
for q in queue2:  # Queue2 contents
    print(q)


# Check if the two queues are equal
if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("queue1 and queue2 are not equal.")

# Change one of the queues

queue2.insert(6)

for q in queue1:  # Queue1 contents
    print(q)

for q in queue2:  # Queue2 contents
    print(q)
# Check if the queues are still equal
if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("After modification, queue1 and queue2 are not equal.")
