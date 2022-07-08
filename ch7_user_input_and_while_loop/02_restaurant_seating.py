"""Restaurant Seating: 
Write a program that asks the user how many people are in their dinner group. 
If the answer is more than eight, print a message saying they’ll have to wait for a table. 
Otherwise, report that their table is ready.
"""

# Get user input
people = int(input("How many people are in their dinner group? "))

# print
if people > 8:
    print(f"They’ll have to wait for a table.")
else:
    print(f"Table is ready.")
