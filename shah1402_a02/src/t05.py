"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports

from Food_utilities import food_search
from Food import Food
# Constants


f = Food("pie", 3, True, 600)
f2 = Food("apple", 3, True, 7)
f3 = Food("Dumpling", 1, False, 6)
f4 = Food("orange", 3, False, 12)
f5 = Food("carrot", 4, True, 9)
f6 = Food("broccoli", 2, True, 11)
f7 = Food("grapes", 1, True, 15)
f8 = Food("tomato", 2, True, 7)
f9 = Food("strawberry", 5, True, 2)
f10 = Food("spinach", 3, True, 5)
f11 = Food("blueberry", 1, True, 8)

# List of Food objects
foods = [f, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11]

results = food_search(foods, 1, 7, False)

for i in results:
    print(i)
