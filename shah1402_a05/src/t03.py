"""
-------------------------------------------------------
List_array Testing 
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list
# Constants

source = List()
source2 = List()
value = [1, 2, 4, 9]
valuet = [1, 2, 3, 5]
for i in range(len(value)):
    source.append(value[i])
print(source._values)

for i in range(len(valuet)):
    source2.append(valuet[i])
print(source2._values)

# Equals Test
print("Equals Test")
equal = source == source2
print(equal)

# __GetItem Test
print("Get item Test")
#value = source[-1]
# print(value)
print("Combine Test")
target1 = List()
#target1.combine(source, source2)
print(target1._values)
print("clean Test")
# source.clean()
# print(source._values)

print("Intersection test:")
target2 = List()
#target2.intersection(source, source2)
#print("Intersection result in source2:", target2._values)

print("Prepend Test")
# source.prepend(-12)
# print(source._values)

print("remove front test")
#value = source.remove_front()
# print(value)

print('remove many test')
# source.remove_many(-12)
# print(source._values)

print("split  Test")
#target3, target4 = source.split()
# print(target3._values)
# print(target4._values)

print("Split alt Test")
#target5, target6 = source.split_alt()
# print(target5._values)
# print(target6._values)

print("Union Test")
source4 = List()
value4 = [1, 2, 3]
for i in range(len(value4)):
    source4.append(value4[i])

source5 = List()
value5 = [1, 2, ]
for i in range(len(value5)):
    source5.append(value5[i])
target45 = List()
print("Union Test")
target45.union(source4, source5)
print(target45._values)
