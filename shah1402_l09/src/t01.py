"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from Food_utilities import read_foods
from functions import hash_table
# Constants


fv = "foods.txt"
f = open(fv, "r", encoding="utf-8")
foods = read_foods(f)
hash_table(7, foods)
f.close()

h = Hash_Set(5)
l = [99, 11, 22, 33, 66]
for i in l:
    h.insert(i)
h.debug()
