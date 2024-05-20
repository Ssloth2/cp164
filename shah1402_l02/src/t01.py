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
# Constants
stack = Stack()

print("Is the stack empty? ", stack.is_empty())

stack.push(2)
stack.push(3)

print("Is the stack empty after pushing elements? ", stack.is_empty())

top_element = stack.peek()
print("Top element (peek): ", top_element)

popped_element = stack.pop()
print("Popped element: ", popped_element)

new_top_element = stack.peek()
print("New top element after popping: ", new_top_element)

print("Elements in the stack from top to bottom:")

for element in stack:
    print(element)
