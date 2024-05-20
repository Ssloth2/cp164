"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants


l = List()

l.append(1)
l.append(2)
l.append(2)
l.append(4)
l.append(5)
l.append(2)
key = 2
p, c, i = l._linear_search_r(key)
print(p._value, c._value, i)
