"""No Users: 
Add an if test to hello_admin.py to make sure the list of users is not empty.
"""

users = []

# If the list is empty, print the message We need to find some users!
if not users:
    print("We need to find some users!")
else:
    for person in users:
        if person == "Admin":
            print(f"Hello {person.lower()}, would you like to see a status report?")
        else:
            print(f"Hello {person}, thank you for logging in again.")