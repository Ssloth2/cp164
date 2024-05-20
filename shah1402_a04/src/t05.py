"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports

from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq_capacity = int(input("Enter the PQ capacty:"))
for i in range(pq_capacity):
    pq.insert(i)

# Define a key to split the priority queue
split_key = int(input("Enter key:"))

# Split the priority queue based on the key
higher_priority, lower_or_equal_priority = pq_split_key(pq, split_key)

print("Target 1 Queue:")
for value in higher_priority:
    print(value, end=' ')
print()

print("Target 2 Queue:")
for value in lower_or_equal_priority:
    print(value, end=' ')
print()
