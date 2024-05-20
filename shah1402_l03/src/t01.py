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

q = Queue()

elements = []

print("Inserting elements into the queue:")
for element in elements:
    print(f"Inserting {element} into the queue.")
    q.insert(element)
    print(f"Queue now contains: {[val for val in q]}")
