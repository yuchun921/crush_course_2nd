"""Glossary 2: 
Now that you know how to loop through a dictionary, 
    clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that \
    runs through the dictionary’s keys and values. 
When you’re sure that your loop works, add five more Python terms to your glossary. 
When you run your program again, these new words and meanings should automatically be included in the output.
"""

glossary = {
    "max": "Return the largest item in an iterable or the largest of two or more arguments.",
    "min": "Return the smallest item in an iterable or the smallest of two or more arguments",
    "sum": "Sums start and the items of an iterable from left to right and returns the total.",
    "append": "Add an item to the end of the list.",
    "get": "Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None.",
    "loop": "Work through a collection of items, one at a time.",
    "dictionary": "A collection of key-value pairs.",
    "key": "The first item in a key-value pair in a dictionary.",
    "value": "An item associated with a key in a dictionary.",
    "conditional test": "A comparison between two values.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}(): {meaning}")
