"""Movie Tickets: 
A movie theater charges different ticket prices depending on a person’s age. 
If a person is under the age of 3, the ticket is free; \
    if they are between 3 and 12, the ticket is $10; \
    and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
"""

prompt = "How old are you? \nEnter 'quit' when you are finished. "

# Get user input: person’s age
while True:
    age = input(prompt)

    # Enter 'quit' when you are finished.
    if age == "quit":
        break

    age = int(age)
    # Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
    if age < 3:
        print(f"Ticket is free.")
    elif 3 <= age < 12:
        print(f"Ticket is $10.")
    else:
        print(f"Ticket is $15.")
