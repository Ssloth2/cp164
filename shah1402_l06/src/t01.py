"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()
# empty test
b = lst.is_empty()
print(f"Is the list empty:{b}")
# len test
n = len(lst)
print(f"List Length: {n}")
# prepend test
value1 = 2
lst.prepend(value1)
print(f"List prepending {value1}")
for l in lst:
    print(l)
print()
# append test
value2 = 34
lst.append(value2)
print(f"list appending {value2}")
for l in lst:
    print(l)
print()
# insert test
in_index = 1
value3 = 1
lst.insert(in_index, value3)
print(f"List inserting {value2} at {in_index}")
for l in lst:
    print(l)
print()
# count test
count_val = 1
c = lst.count(count_val)
print(f"The number of {count_val}'s in the list is:{c}")
print()
# max test
max_value = lst.max()
print(f"max val:{max_value}")
print()
# min test
min_value = lst.min()
print(f"max val:{min_value}")
print()
# find dtest
value_to_find = 0
value_find = lst.find(value_to_find)
print(f"Find:{value_find}")
print()
# index Test
index_key = 2
n = lst.index(index_key)
print(f"index:{index_key}")
print()

# Contains Test
contain_key = 1
b = contain_key in lst
print(f"contains {contain_key}:{b}")
print()
# peek
peek_value = lst.peek()
print(f"Peek number:{peek_value}")
# remove
remove_val = 34
value_remove = lst.remove(remove_val)
print()
print(f"removed value: {value_remove}")
for l in lst:
    print(l)
# __getitem_
get_index = -1
get_value = lst[get_index]
print(f"Get item: {get_value}")
# __setitem__
set_index = 0
set_value = 204
lst[set_index] = set_value

print(f"set index{set_index} to {set_value}:")
for l in lst:
    print(l)
