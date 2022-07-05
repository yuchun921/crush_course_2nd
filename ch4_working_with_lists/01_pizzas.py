"""Pizzas: 
Think of at least three kinds of your favorite pizza. 
Store these pizza names in a list, and then use a for loop to print the name of each pizza.
"""

pizzas_favor = ["Hawaiian", "Neapolitan", "Pepperoni"]

# Use a for loop to print the name of each pizza
for pizza in pizzas_favor:
    print(pizza)

print("--------------------")
# Print a sentence using the name of the pizza instead of printing just the name of the pizza.
# For each pizza you should have one line of output containing a simple statement like "I like pepperoni pizza."
for pizza in pizzas_favor:
    print(f"I like {pizza} pizza.")

# Add a line at the end of your program, outside the for loop
print("I really love pizza!")
