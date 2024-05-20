"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_food
# Constants
s = Stack()

fh = open("foods.txt", "r", encoding="utf-8")

for line in fh:
    food = read_food(line)
    s.push(food)


stack_test(s)

fh.close()
