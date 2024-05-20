"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
-------------------------------------------------
"""
# Imports
from functions import matrixes_add
# Constants


row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))


a = []
for i in range(row):
    row_temp = []
    for j in range(col):
        a_temp = int(input("Enter a number for matrix a:"))
        row_temp.append(a_temp)
    a.append(row_temp)

b = []
for i in range(row):
    row_temp = []
    for j in range(col):
        b_temp = int(input("Enter a number for matrix b:"))
        row_temp.append(b_temp)
    b.append(row_temp)

c = matrixes_add(a, b)
print(c)
