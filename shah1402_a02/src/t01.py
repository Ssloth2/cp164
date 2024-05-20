"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import by_origin
from Food import Food

# Constants


f = Food(" Egg Fried Rice", 0, True, 250)
f2 = Food("wonton", 0, False, 77)
f3 = Food("Dumplings", 0, False, 60)

foods = [f, f2, f3]

o_foods = by_origin(foods, 0)

for i in o_foods:
    print(i)
