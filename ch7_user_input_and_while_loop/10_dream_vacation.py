"""Dream Vacation: 
Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where would you go?
Include a block of code that prints the results of the poll.
"""

place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "Would you like to let someone else respond? (yes/no) "

records = {}
while True:
    # Asking user where like to go?
    user = input("What's your name? ")
    location = input(place_prompt)
    
    # store info to recode
    records[user] = location
    
    # Asking someone need to respond?
    ask_again = input(continue_prompt)
    
    if ask_again.lower() == "no":
        break

print()
for name, place in records.items():
    print(f"{name.title()} would like to go to {place.title()}.")
    