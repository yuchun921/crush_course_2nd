"""Changing Guest List:
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.
"""

# 3-4 guest list
guests = ["Abby", "Tom", "Grace"]

print(f"Hi, {guests[0]}, welcome to dinner.")
print(f"Hi, {guests[1]}, welcome to dinner.")
print(f"Hi, {guests[2]}, welcome to dinner.")

# 3-5 changing guest list
# Abby can't come to dinner, change Abby to Dora
print(f"{guests[0]} can't come to dinner.")

guests[0] = "Dora"

print(f"Hi, {guests[0]}, welcome to dinner.")
print(f"Hi, {guests[1]}, welcome to dinner.")
print(f"Hi, {guests[2]}, welcome to dinner.")