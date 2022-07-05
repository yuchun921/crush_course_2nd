"""My Pizzas, Your Pizzas: 
Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. 
Then, do the following:
"""

my_pizzas = ["Hawaiian", "Neapolitan", "Pepperoni"]

# Make a copy of the list of pizzas, and call it friend_pizzas.
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list.
my_pizzas.append("Pineapple")

# Add a different pizza to the list friend_pizzas.
friend_pizzas.append("Seafood")

# Make sure each newpizza is stored in the appropriate list.
# Print the message "My favorite pizzas are:", and then use a for loop to print the first list. 
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza) 
    
# Print the message "My friend’s favorite pizzas are:", and then use a for loop to print the second list. 
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza) 