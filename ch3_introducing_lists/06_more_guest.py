"""More Guests: 
You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.
"""

# 3-4 guest list
guests = ["Abby", "Tom", "Grace"]

print(f"Hi, {guests[0]}, welcome to dinner.")
print(f"Hi, {guests[1]}, welcome to dinner.")
print(f"Hi, {guests[2]}, welcome to dinner.")

# 3-5 changing guest list
# Abby can't come to dinner, change Abby to Dora
print("--------------------------")
print(f"{guests[0]} can't come to dinner.")

guests[0] = "Dora"

print(f"Hi, {guests[0]}, welcome to dinner.")
print(f"Hi, {guests[1]}, welcome to dinner.")
print(f"Hi, {guests[2]}, welcome to dinner.")

# 3-6 more guest
# find a bigger table
print("--------------------------")
print("Hi, I found a bigger dinner table.")

guests.insert(0, "Ben")
guests.insert(int(len(guests)/2), "Robin")
guests.append("Nick")

for p in guests:
    print(f"Hi, {p}, welcome to dinner.")