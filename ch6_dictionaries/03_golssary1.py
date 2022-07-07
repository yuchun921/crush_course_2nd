"""Glossary: 
A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
"""

# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values
glossary = {
    "max": "Return the largest item in an iterable or the largest of two or more arguments.",
    "min": "Return the smallest item in an iterable or the smallest of two or more arguments",
    "sum": "Sums start and the items of an iterable from left to right and returns the total.",
    "append": "Add an item to the end of the list.",
    "get": "Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None.",
}

# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, 
# or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
print(f"max(): {glossary['max']}")
print(f"Min(): {glossary['min']}")
print(f"Sum(): {glossary['sum']}")
print(f"Append(): {glossary['append']}")
print(f"Get(): {glossary['get']}")


