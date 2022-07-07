"""Favorite Places: 
Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.
"""

# Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
favorite_places = {
    "Penny": ["keelung", "taipei", "taoyuan"],
    "Louis": ["hsinchu", "miaoli"],
    "Jack": ["chiayi", "tainan", "pingtung"],
}

# Loop through the dictionary, and print each person’s name and their favorite places.
for people, locations in favorite_places.items():
    print(f"{people} likes the following places:")
    for location in locations:
        print(f"- {location.title()}")
