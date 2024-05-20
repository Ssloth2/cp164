"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants


stack = Stack()

source = []

print("Source array before transferring to stack:", source)

array_to_stack(stack, source)

print("Source array after transferring to stack:", source)

print("Elements in the stack from top to bottom:")
for element in stack:
    print(element)
