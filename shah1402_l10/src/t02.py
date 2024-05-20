"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-22"
-------------------------------------------------------
"""
# Imports
from test_Sorts_List_linked import test_sort
from Sorts_List_linked import Sorts

print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),

)

test_sort(SORTS[0][0], SORTS[0][1])
test_sort(SORTS[1][0], SORTS[1][1])
test_sort(SORTS[2][0], SORTS[2][1])
test_sort(SORTS[3][0], SORTS[3][1])
test_sort(SORTS[4][0], SORTS[4][1])
test_sort(SORTS[5][0], SORTS[5][1])
test_sort(SORTS[6][0], SORTS[6][1])
test_sort(SORTS[7][0], SORTS[7][1])
test_sort(SORTS[8][0], SORTS[8][1])
test_sort(SORTS[9][0], SORTS[9][1])
test_sort(SORTS[10][0], SORTS[10][1])
