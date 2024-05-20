"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from Stack_array import Stack
#  Constants


source1 = Stack()
source2 = Stack()
len1 = int(input("Enter the size of source1:"))
for i in range(len1):
    source1.push(int(input("Enter a number to push:")))
print("Source1 is:")
for p in source1:
    print(p)
print("")
len2 = int(input("Enter the size of source2:"))
for i in range(len2):
    source2.push(int(input("Enter a number to push:")))
print("Source2 is:")
for p in source2:
    print(p)
print("")
target = stack_combine(source1, source2)
print("Target has:")
for t in target:
    print(t)
