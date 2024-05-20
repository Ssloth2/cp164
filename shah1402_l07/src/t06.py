"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

original_list = List()
for value in range(1, 6):  # This will create a list with values 1 to 5
    original_list.append(value)

# Display the original list order.
print("Original List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

# Reverse the list using the recursive method.
original_list.reverse_r()

# Display the reversed list order.
print("Reversed List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()
l = List()
l.append(22)
l.append(33)
l.append(11)
l.append(55)
l.append(44)
l.append(None)

l.reverse_r()

print(l._rear._value, l._front._value, l._front._next._value, l._front._next._next._value,
      l._front._next._next._next._value, l._front._next._next._next._next._value, l._front._next._next._next._next._next._value)
