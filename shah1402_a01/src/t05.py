"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
-------------------------------------------------
"""
# Imports
from functions import is_leap_year
# Constants

year = int(input("Enter the year:"))
leap_year = is_leap_year(year)
print(leap_year)
