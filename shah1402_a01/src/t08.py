"""
-------------------------------------------------------
t08
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
-------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants


rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns"))
a = []
for i in range(rows):
    row_temp = []
    for j in range(cols):
        a_temp = int(input("Enter a number:"))
        row_temp.append(a_temp)
    a.append(row_temp)


small, large, total, average = matrix_stats(a)
print(small)
print(large)
print(total)
print(average)
