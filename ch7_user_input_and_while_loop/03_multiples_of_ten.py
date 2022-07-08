"""Multiples of Ten: 
Ask the user for a number, and then report whether the number is a multiple of 10 or not.
"""

# Get user input
num = int(input("Give a num: "))

# Output
if num % 10 == 0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")
