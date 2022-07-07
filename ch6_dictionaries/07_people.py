"""People:
Start with the program you wrote for Exercise 6-1 (page 102). 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. 
As you loop through the list, print everything you know about each person.
"""

p1_info = {
    "first_name": "Peggy",
    "last_name": "Chen",
    "age": 26,
    "city": "Hsinchu",
}

# Make two new dictionaries representing different people
p2_info = {
    "first_name": "Yoga",
    "last_name": "Chiu",
    "age": 42,
    "city": "Taipei",
}

p3_info = {
    "first_name": "Robin",
    "last_name": "Haung",
    "age": 38,
    "city": "Tainan",
}

# store all three dictionaries in a list called people
people = []
people.append(p1_info)
people.append(p2_info)
people.append(p3_info)

# Loop through your list of people and print everything you know about each person
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person["age"]
    city = person["city"].title()

    print(f"{name}, of {city}, is {age} years old.")
