# Angel Chavez
# Jul 19th, 2025
# Python 3.13.5
# Body Mass Index calculator, based on weight and height

print('---- BMI Calculator ----')

# prompt user for data
weight = float(input('Enter your current weight(Kilograms): '))
height = float(input('Enter your current height(Meters): '))

# formula for BMI
body_mass_index = weight / (height ** 2)

# output calculations
print(f'Your current BMI is: {body_mass_index:.1f}Kg/m squared')