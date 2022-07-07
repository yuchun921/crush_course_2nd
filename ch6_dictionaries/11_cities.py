"""Cities:
Make a dictionary called cities. 
Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, \
    its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.
"""

# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city.
cities = {
    "santiago": {
        "country": "chile",
        "population": 5_220_161,
        "altitude": 520,
    },
    "talkeetna": {
        "country": "united states",
        "population": 876,
        "altitude": 106,
    },
    "kathmandu": {
        "country": "nepal",
        "population": 2_900_000,
        "altitude": 1_400,
    },
}
# Print the name of each city and all of the information you have stored about it.
for city, infos in cities.items():
    country = infos["country"]
    population = infos["population"]
    altitude = infos["altitude"]

    print(f"The {city.title()} in {country.title()}.")
    print(f"  it has a population of about {population}.")
    print(f"  and it is located at {altitude} meters above sea level.")
