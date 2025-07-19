# Angel Chavez
# Jul 19th, 2025
# Python 3.13.5
# CHALLENGE-LAB: paint project cost estimator based on size/area of project and cost of paint.
# 

import math

print('---- Paint Project Cost Estimator ----')

# prompts user for data needed for calculations
width = float(input('Enter the width of the wall in feet: '))
height = float(input('Enter the height of the wall in feet: '))
coverage_per_gallon = float(input('Enter the coverage of paint per gallon(sq ft): '))
price_per_gallon =  float(input('Enter the price of paint per gallon(USD): '))

# formula for area of wall, amount of paint needed, and total cost
wall_area = width * height
paint_gallon_needed = math.ceil(wall_area / coverage_per_gallon)
total_cost = paint_gallon_needed * price_per_gallon

# print out to the screen
print(f'Wall area: {wall_area:.0f}sq ft')
print(f'Amount of gallon(s) needed: {paint_gallon_needed}')
print(f'Total cost: ${total_cost:.2f}')