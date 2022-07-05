"""Threes:
Make a list of the multiples of 3 from 3 to 30. 
Use a for loop to print the numbers in your list.
"""

nums = list(range(3, 31))
for i in nums:
    if i % 3 == 0:
        print(i)
