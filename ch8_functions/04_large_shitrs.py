"""Large Shirts:
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""


def make_shirt(size, message="I love Python"):
    print(f"I make a {size} size t-shirt, will print {message} on it.")


def main():
    # Make a large shirt and a medium shirt with the default message
    make_shirt("L")
    make_shirt("M")

    # Make a shirt of any size with a different message
    make_shirt(size="XS", message="Wonderful T-shirt")


if __name__ == "__main__":
    main()
