"""
-------------------------------------------------------
Sorting List Testing 
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
# Constants
source1 = Sorted_List()
value1 = [-3, 4, 3, 43, 35, 3, 34, 5, 3, 4,
          5, 4, 3, 6, 7, 8, 6, 89, 8, 7, 44056]
for i in range(len(value1)):
    source1.insert(value1[i])
print(source1._values)

source2 = Sorted_List()
value2 = [44056, 57, 8, 6, 89, 8, 7]
for i in range(len(value2)):
    source2.insert(value2[i])
print(source2._values)
print("Contains Test")
b = 2 in source1
print(b)

print("Eqauls Test")
equals = source1 == source2
print(equals)

print("Get item")
#value = source1[2]
# print(value)

print("clean test")
source1.clean()
print(source1._values)

print("count Test")
n = source1.count(3)
print(n)
print("find Test")
value = source1.find(102)
print(value)

print("index Test")
n = source1.index(102)
print(n)

print("max Test")
value = source1.max()
print(value)

print("min Test")
value = source1.min()
print(value)

print("peek Test")
value = source1.peek()
print(value)

print("remove_font Test")
value = source1.remove_front()
print(value)

source1.remove_many(3)
print(source1._values)

print("remove Test")
value = source1.remove(43)
print(source1._values)

#print(" intersectionTest")
#target = Sorted_List()
#target.intersection(source1, source2)
# print(target._values)

#print('split Test')
source3 = Sorted_List()
value3 = [1, 2, 34, 3, 3, 3, 3, 34, 34, 94, ]
for i in range(len(value3)):
    source3.insert(value3[i])
#target1, target2 = source3.split()
# print(target1._values)
# print(target2._values)

#print("split al Test")
#arget1, target2 = source3.split_alt()
# print(target1._values)
# print(target2._values)

#print(" split key test ")
#target1, target2 = source3.split_key(34)
# print(source3._values)
# print(target1._values)
# print(target2._values)


source4 = Sorted_List()
value4 = [1, 2, 3]
for i in range(len(value4)):
    source4.insert(value4[i])

source5 = Sorted_List()
value5 = [1, 2, ]
for i in range(len(value5)):
    source5.insert(value5[i])
target45 = Sorted_List()
print("Union Test")
target45.union(source4, source5)
print(target45._values)
