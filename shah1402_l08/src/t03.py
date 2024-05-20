"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports

# Constants


from BST_linked import BST
from morse import fill_letter_bst, DATA1

bst = BST()

fill_letter_bst(bst, DATA1)

for each in bst.inorder():
    print(each)
