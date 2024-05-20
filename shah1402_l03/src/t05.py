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

# Constants


from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

pq.insert(30)


while not pq.is_empty():
    highest_priority_value = pq.remove()
    print("Removed:", highest_priority_value)

print()

q = Priority_Queue()

q.insert("Mango")


# Remove and display the highest priority string (alphabetically first)
while not q.is_empty():
    highest_priority_value1 = q.remove()
    print("Removed:", highest_priority_value1)
