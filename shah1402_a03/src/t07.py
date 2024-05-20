"""
-------------------------------------------------------
t07
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports

from Stack_array import Stack
from functions import stack_maze

# Constants

maze = {
    'Start': ['A'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['X'],
    'E': ['F'],
    'F': ['G'],
    'G': ['C']
}

print(maze)

# Expected output: ['A', 'C', 'E', 'X']
print(stack_maze(maze))
