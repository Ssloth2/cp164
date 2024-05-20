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
from utilities import stack_test
# Constants


source_data = Stack()

source_data.push(1)
source_data.push(2)
source_data.push(3)


stack_test(source_data)

print("\nTesting with an empty source list:")
empty_source_data = Stack()
stack_test(empty_source_data)
