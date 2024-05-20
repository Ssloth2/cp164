"""
-------------------------------------------------------
functions
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports

# Constants


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """

    print("""
    Hashes
    Hash     Slot Key
    -------- ---- --------------------  """)
    for v in values:
        h = hash(v)
        slot = h % slots
        formatted_string = v.key()
        print("{:8}{:5} {}".format(h, slot, formatted_string))

    return
