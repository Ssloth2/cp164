"""
-------------------------------------------------------
Writing 
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods, get_food
# Constants


file_variable = open("new_foods.txt", "a", encoding="utf-8")


foods = []

foods.append(get_food())


write_foods(file_variable, foods)
file_variable.close()
