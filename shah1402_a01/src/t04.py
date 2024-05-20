"""
-------------------------------------------------------
t04
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
-------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants


fv = open("file_testing", "r", encoding="utf-8")

upp, low, dig, whi, rem = file_analyze(fv)
print(f"Upper Letters:{upp}")
print(f"Lower letters:{low}")
print(f"Digits:{dig}")
print(f"White Space:{whi}")
print(f"Remainder:{rem}")
fv.close()
