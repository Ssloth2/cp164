"""
-------------------------------------------------------
Food class definition.
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports

from Queue_array import Queue
from utilities import queue_test
from utilities import queue_to_array
from utilities import array_to_queue

q = Queue()

source = [1, 2, 3]
print("Original source array:", source)

array_to_queue(q, source)
print("Source array after populating queue:", source)
print("Queue after populating from source:", [val for val in q])

target = []
queue_to_array(q, target)
print("Queue after transferring to target array:", [val for val in q])
print("Target array after receiving queue contents:", target)

print("\nTesting queue operations:")
test_data = [1, 2, 3]
queue_test(test_data)
