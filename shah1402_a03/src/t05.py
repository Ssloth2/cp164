"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack
# Constants
string = input("Enter a string:")
palindrome = is_palindrome_stack(string)
print(f"Is {string} a palindrome:{palindrome}")
