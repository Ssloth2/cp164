"""
-------------------------------------------------------
A08 t03
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports

from Letter import fill_letter_bst
from BST_linked import BST
from functions import letter_table, do_comparisons, comparison_total
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
bst2 = BST()
fill_letter_bst(bst2, DATA2)
fv = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(fv, bst2)
t2 = comparison_total(bst2)
letter_table(bst2)
