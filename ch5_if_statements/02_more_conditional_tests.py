"""More Conditional Tests: 
You don’t have to limit the number of tests you create to ten. 
If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following:
"""

a = "apple"
b = "Banana"
fruit = ["apple", "mango"]

# Tests for equality and inequality with strings
print(f"a eaqul to b ? {a==b}")

# Tests using the lower() method
print(f"Lower b eaqul to b ? {b.lower()==b}")

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
print(f"a of lenthg greater than b of length ? {len(a)>len(b)}")
print(f"a of lenthg eaqul to b of length ? {len(a)==len(b)}")
print(f"b of lenthg greater than a of length ? {len(b)>len(a)}")

# Tests using the and keyword and the or keyword
print(f"a eaqul to 'apple' and b eaqul to 'Banana' ? {a == 'apple' and b == 'Banana'}")
print(f"a eaqul to 'apple' or b eaqul to 'cherry' ? {a == 'apple' or b == 'banana'}")

# Test whether an item is in a list
print(f"whether an apple is in a list ? {a in fruit}")

# Test whether an item is not in a list
print(f"whether an papaya is not in a list ? {'papaya' not in fruit}")
