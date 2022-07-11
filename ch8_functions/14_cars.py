"""Cars:
Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name.
It should then accept an arbitrary number of keyword arguments.
Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
Your function should work for a call like this one:
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.
"""


def store_car_info(manufacturer, model_name, **info):
    """Make a dictionary representing a car."""
    car_infos = {
        "manufacturer": manufacturer,
        "model_name": model_name
    }

    for title, item in info.items():
        car_infos[title] = item

    return car_infos


def main():
    car1 = store_car_info('ford', 'focus', color='blue', tow_package=True)
    car2 = store_car_info('mazda', 'accord', year=1991, color='white', headlights='popup')
    print(f"CAR1 info: {car1}")
    print(f"CAR2 info: {car2}")


if __name__ == "__main__":
    main()
