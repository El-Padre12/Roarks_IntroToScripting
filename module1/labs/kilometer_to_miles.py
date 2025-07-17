# Angel Chavez
# Jul 17th, 2025
# Python 3.13.5
# simple distance converter (Kilometer -> Miles)

# stores input as a float
kilometers = float(input('Input the distance in Kilometers: '))

# formula for converting kilometers to miles
miles = kilometers * 0.621371

# outputs the solution using two decimal places.
print(f'{kilometers} Kilometers is {miles:.2f} Miles.')