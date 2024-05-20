"""
-------------------------------------------------------
t04
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports

from Queue_array import Queue

source_queue = Queue()
list = []
# Fill the source queue with some values
for i in range(0):
    source_queue.insert(i)
print("Source: Contents")
for s in source_queue:
    list.append(s)
print(list)

# Split the source queue into two alternating queues
target1, target2 = source_queue.split_alt()

# Display the resulting queues
print("Target 1 Queue:")
for value in target1:
    print(value, end=' ')
print()

print("Target 2 Queue:")
for value in target2:
    print(value, end=' ')
print()
