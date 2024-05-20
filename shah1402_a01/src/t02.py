"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
-------------------------------------------------
"""
# Imports
from functions import list_subtraction
# Constants


minuend = []
subtrahend = []

min_len = int(input("Enter the length of the minuend:"))
for i in range(min_len):
    min_temp = int(input("Enter a value:"))
    minuend.append(min_temp)


sub_len = int(input("Enter the length of the subtrahend:"))
for i in range(sub_len):
    sub_temp = int(input("Enter a value:"))
    subtrahend.append(sub_temp)

print(f"Minuend: {minuend}")
print(f"Subtrahend: {subtrahend}")
print()


list_subtraction(minuend, subtrahend)
