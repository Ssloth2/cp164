"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants


my_list = List()

my_list.append(10)
my_list.append(20)
my_list.append(30)

second_item = my_list[1]
print(f"The second item in the list: {second_item}")

print("Setting the second item in the list to 25...")
my_list[1] = 25

try:
    print("Trying to access index out of range:")
    my_list[5]
except AssertionError as e:
    print(f"Error: {e}")

try:
    print("Trying to set index out of range:")
    my_list[5] = 50
except AssertionError as e:
    print(f"Error: {e}")
