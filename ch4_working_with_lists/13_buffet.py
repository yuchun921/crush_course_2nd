"""Buffet:
A buffet-style restaurant offers only five basic foods. 
Think of five simple foods, and store them in a tuple.
"""

buffet_foods = ("mango", "straberry", "grape", "apple", "banana")

# Use a for loop to print each food the restaurant offers.
for food in buffet_foods:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the change.
# cause TypeError: 'tuple' object does not support item assignment: 
#   buffet_foods[2] = "papaya"

print("--------------------------------")

# The restaurant changes its menu, replacing two of the items with different foods.
buffet_foods = ("mango", "straberry", "cherry", "apple", "orange")
# Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
for food in buffet_foods:
    print(food)
