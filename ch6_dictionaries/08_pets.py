"""Pets: 
Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet.
"""

# In each dictionary, include the kind of animal and the owner’s name.
pet1 = {
    "type": "Dog",
    "name": "Uni",
    "owner": "Gill",
}

pet2 = {
    "type": "Cat",
    "name": "Kiki",
    "owner": "Dan",
}

pet3 = {
    "type": "Bird",
    "name": "Sushi",
    "owner": "Wendy",
}

# Store these dictionaries in a list called pets.
pets = [pet1, pet2, pet3]

# Loop through your list and as you do, print everything you know about each pet
for pet in pets:
    animal_type = pet["type"]
    name = pet["name"]
    owner = pet["owner"]

    print(f"The pet name is {name}, it is a {animal_type}, and it's owner is {owner}.")
