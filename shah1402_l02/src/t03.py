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
from utilities import stack_to_array

# Constants

stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)


target = []

stack_to_array(stack, target)

print("Is the stack empty after transferring to array? ",
      stack.is_empty())  # Should be True

print("Elements in the target array:", target)
