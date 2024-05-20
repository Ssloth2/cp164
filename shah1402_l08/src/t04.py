"""
-------------------------------------------------------
t04
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
from morse import fill_code_bst, DATA1

bst = BST()

# Fill the BST with Morse code data
fill_code_bst(bst, DATA1)

# Print the BST
print("BST Contents in Inorder:")
for each in bst.inorder():
    print(each)
