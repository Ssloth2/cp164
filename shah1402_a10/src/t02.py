"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List

a = List()
a.append(6)
a.append(34)
a.append(34)
a.append(342)
a.append(4)
a.append(1)
a.append(3)
a.append(35)
a.append(52)
a.append(12343120)
a.append(34)
a.append(3429)
unsorted = []
for n in a:
    unsorted.append(n)

print(f"Unsorted:{unsorted}")
Sorts.radix_sort(a)
sorted = []
for sort_n in a:
    sorted.append(sort_n)
print(f"Sorted{sorted}")
