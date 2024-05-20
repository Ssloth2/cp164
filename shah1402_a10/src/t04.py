"""
-------------------------------------------------------
t04
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_rear(--3)
a.insert_rear(1)
a.insert_rear(2343441)
a.insert_rear(104)
a.insert_rear(-235)
a.insert_rear(932493)
a.insert_rear(0)
a.insert_rear(-1)
a.insert_rear(-1)

Sorts.gnome_sort(a)

for i in a:
    print(i)
