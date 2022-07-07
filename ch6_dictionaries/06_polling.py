"""Polling: 
Use the code in favorite_languages.py (page 97).
"""

# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
persons = ["Penny", "Louis", "Jack", "Una", "Grace"]

favorite_languages = {
    "Jack": "python",
    "Sarah": "c",
    "Edward": "ruby",
    "Grace": "python",
}

# Loop through the list of people who should take the poll.
# If they have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll
for name in persons:
    if name in favorite_languages:
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, what's your favorite programming language?")
