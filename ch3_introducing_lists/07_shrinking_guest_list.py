"""Shrinking Guest List: 
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
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
    
# 3-7 shrinking guest list
print("--------------------------")
print("Hi, new dinner table won’t arrive in time for the dinner, so I have space for only two guests.")

while len(guests) > 2:
    print(f"Hi, {guests.pop()}, I'm sorry that I don't have enough space to invite you.")
    
for p in guests:
    print(f"Hi, {p}, welcome to dinner.")

del guests[1]
del guests[0]
print(guests)
