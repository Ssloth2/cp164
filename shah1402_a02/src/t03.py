"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import calories_by_origin
from Food import Food
# Constants


f = Food("grape", 1, True, 120)
f2 = Food("apple", 1, True, 7)
f3 = Food("banana", 1, True, 6)
f4 = Food("orange", 2, False, 5)
f5 = Food("carrot", 3, True, 3)

foods = [f, f2, f3, f4, f5]

by_origin = calories_by_origin(foods, 1)

print(by_origin)
