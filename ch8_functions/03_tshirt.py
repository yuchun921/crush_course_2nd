"""T-Shirt:
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
"""


def make_shirt(size, message):
    print(f"I make a {size} size t-shirt, will print {message} on it.")


def main():
    # Call the function once using positional arguments to make a shirt.
    make_shirt("M", "Hello T-shirt")

    # Call the function a second time using keyword arguments.
    make_shirt(size="L", message="Wonderful T-shirt")


if __name__ == "__main__":
    main()
