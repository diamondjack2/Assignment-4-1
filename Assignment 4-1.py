"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

charge = 0.00
numChars = 20
color = "gold"
woodType = "pine"

# Write assignment and if statements here as appropriate.

charge = 35.00

if numChars > 5:
    charge += (numChars - 5) * 4.00

if woodType == "oak":
    charge += 20.00

if color == "gold":
    charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))