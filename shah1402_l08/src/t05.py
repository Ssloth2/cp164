"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Syed Shah
ID:      169071402
Email:   shah1402@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports

# Constants


from BST_linked import BST
from morse import fill_letter_bst, encode_morse, DATA1

bst = BST()

# Step 2: Fill the BST with Morse code data
fill_letter_bst(bst, DATA1)

# Step 3: Encode a text string into Morse code
text = "HELLO WORLD"
morse_code = encode_morse(bst, text)
print(f"Original Text: {text}")
print(f"Encoded Morse Code: {morse_code}")
