"""
-------------------------------------------------------
Get vegetarian
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import get_vegetarian, read_foods
from Food import Food
# Constants


file_variable = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file_variable)


v_foods = get_vegetarian(foods)

for each in v_foods:
    print(each)
    print()
