"""Favorite Numbers: 
Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
"""

favorite_nums = {
    "Penny": [2, 64, 7, 34],
    "Louis": [4, 8, 56, 93],
    "Jack": [5, 56],
    "Una": [7, 23, 88],
    "Grace": [8, 45, 28, 83],
}

for name, numbers in favorite_nums.items():
    print(f"\n{name.title()} likes the these numbers: ")
    for number in numbers:
        print(f"  {number}")