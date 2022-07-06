"""Hello Admin: 
Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website.
"""

users = ["Penny", "Louis", "Jack", "Admin", "Grace"]

# Loop through the list,
# If the username is 'admin', print a special greeting, such as "Hello admin, would you like to see a status report?"
# Otherwise, print a generic greeting, such as "Hello Jaden, thank you for logging in again."
for person in users:
    if person == "Admin":
        print(f"Hello {person.lower()}, would you like to see a status report?")
    else:
        print(f"Hello {person}, thank you for logging in again.")
