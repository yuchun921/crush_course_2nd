"""Conditional Tests:
Write a series of conditional tests. 
Print a statement describing each test and your prediction for the results of each test. 
Your code should look something like this:
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
"""

car = 'bmw'
cars = ['bmw','ford']

# True
print(car == 'bmw')
print(car == car)
print(car == 'bmw' or  car == 'ford')
print(int(len(car)) == int(len('bmw')))
print('bmw' in cars)

# False
print(car != 'bmw')
print(car == car.title())
print(car == 'bmw' and car == 'ford')
print(int(len(car)) == int(len('ford')))
print('ford' not in cars)
