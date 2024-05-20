"""
-------------------------------------------------------
A08 t03
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-24"
-------------------------------------------------------
"""
# Imports

# Constants

from BST_linked import BST

bst = BST()

bst.insert(1)
bst.insert(21)
bst.insert(321)
bst.insert(4321)
bst.insert(54321)
bst.insert(6542321)

one, two, three = bst.node_counts()

print(one)
print(two)
print(three)

print(321 in bst)

val = bst.parent(20)

val2 = bst.parent_r(20)

print(val, val2)
