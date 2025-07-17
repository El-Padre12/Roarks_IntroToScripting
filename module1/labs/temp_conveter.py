# Angel Chavez
# Jul 17th, 2025
# Python 3.13.5
# simple temperature converter (Fahrenheit -> Celcius)

# stores input from user as a float in a variable called fahrenheit
fahrenheit = float(input('Input the temperature in Fahrenheit: '))

# formula for converting fahrenheit into celcious stored in a variable called celcius
celcius = float(5 / 9 * (fahrenheit - 32))

# prints celcius to the screen using an f-string with ":.2f" allowing us to output the number with 2 decimal places
print(f'the temperature in Celcius is {celcius:.2f} degrees.')