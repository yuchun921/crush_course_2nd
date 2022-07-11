"""Messages:
Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.
"""


def show_messages(messages: list):
    for message in messages:
        print(message)


def main():
    messages: list = [
        "Sometimes you won’t know ahead of time how many arguments a function needs to accept.",
        "Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.",
        "For example, consider a function that builds a pizza. It needs to accept a number of toppings,",
        "but you can’t know ahead of time how many toppings a person will want."
    ]

    show_messages(messages)


if __name__ == "__main__":
    main()
