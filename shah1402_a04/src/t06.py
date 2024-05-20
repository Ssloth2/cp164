"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-06"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(12)
pq.insert(22)
pq.insert(33)
pq.insert(44)
pq.insert(55)

key = 33
print(f"PQ values:{pq._values}")
print(f"Key {key}")
target1, target2 = pq.split_key(key)
print("Target 1:")
for t1 in target1:
    print(t1)
print("Target 2:")
for t2 in target2:
    print(t2)
print(pq._values)
