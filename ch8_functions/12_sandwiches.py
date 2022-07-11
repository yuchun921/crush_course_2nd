"""Sandwiches:
Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides, \
    and it should print a summary of the sandwich that’s being ordered.
Call the function three times, using a different number of arguments each time.
"""


# The function should have one parameter that collects
def make_sandwiches(*items):
    for item in items:
        print(f"Add {item} to sandwiches.")
        print(f"The sandwich is ready.\n")


def main():
    make_sandwiches("beef", "tomato")
    make_sandwiches("peanut butter", "pork", "lettuce", "cucumber")
    make_sandwiches("egg", "smoked chicken", "cheese")


if __name__ == "__main__":
    main()
