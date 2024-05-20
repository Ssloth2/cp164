"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
from Stack_array import Stack
# Constants

source = Stack()
len = int(input("Enter the length of the stack:"))
for i in range(len):
    source.push(int(input("Enter a number:")))
print("")
print("The source contains:")
for s in source:
    print(s)
stack_reverse(source)
print("")
print("The reverse source contains:")
for s in source:
    print(s)
