"""City Names:
Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this: "Santiago, Chile"
"""


def city_country(city_name, country):
    return f"{city_name}, {country}".title()


def main():
    # Call your function with at least three city-country pairs, and print the values that are returned.
    print(city_country("Taipei", "Taiwan"))
    print(city_country("Hsinchu", "Taiwan"))
    print(city_country("Tokyo", "Japan"))


if __name__ == "__main__":
    main()
