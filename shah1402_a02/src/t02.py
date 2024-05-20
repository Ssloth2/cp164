"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food_utilities import average_calories
from Food import Food
# Constants


f = Food("grape", 3, True, 10)
f2 = Food("apple", 3, True, 700)
f3 = Food("banana", 1, True, 1000)

foods = [f, f2, f3]

print(average_calories(foods))
4
