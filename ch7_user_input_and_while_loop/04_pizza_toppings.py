"""Pizza Toppings: 
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

add_toppings = True
while add_toppings:
    toppings = input(prompt)
    if toppings == 'quit':
        add_toppings = False
    else:
        print(f"I’ll add {toppings.title()} to their pizza.")
