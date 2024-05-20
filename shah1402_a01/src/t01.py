"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
-------------------------------------------------
"""
# Imports
from functions import clean_list
# Constants
values = []
list_len = int(input("Enter the length of the list:"))
for i in range(list_len):
    value_i = int(input("Enter a number:"))
    values.append(value_i)
clean_list(values)
print(values)
