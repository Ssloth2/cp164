"""
-------------------------------------------------------
Read Foods
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
# Constants


file_variable = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file_variable)

for each in foods:
    print(each)
    print()

file_variable.close()
