"""
-------------------------------------------------------
t07
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import list_test
from List_array import List

# Constants


llist = List()

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

for each in foods:
    llist.append(each)


list_test(llist)
