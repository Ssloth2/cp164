"""
-------------------------------------------------------
t07
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
-------------------------------------------------
"""
# Imports
from functions import max_diff
# Constants

list_length = int(input("Enter a the list length:"))
a = []
for i in range(list_length):
    a_temp = int(input("Enter a number:"))
    a.append(a_temp)

md = max_diff(a)
print(md)
