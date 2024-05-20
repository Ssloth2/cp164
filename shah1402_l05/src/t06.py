"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""
# Imports
from functions import bag_to_set
# Constants
bag = []
bag_length = int(input("How many things are in are bag?:"))
for i in range(bag_length):
    bag_i = input("Enter something:")
    bag.append(bag_i)
print(f"Bag:{bag}")
new_set = bag_to_set(bag)
print(f"New Bag: {new_set}")
