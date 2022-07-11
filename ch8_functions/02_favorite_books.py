"""Favorite Book:
Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as One of my favorite books is Alice in Wonderland.
Call the function, making sure to include a book title as an argument in the function call.
"""


def favorite_book(title: str):
    print(f"One of my favorite books is {title.title()}.")


def main():
    favorite_book("The Thursday Murder Club")


if __name__ == "__main__":
    main()
