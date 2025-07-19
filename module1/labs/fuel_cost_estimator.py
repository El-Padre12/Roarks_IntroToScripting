# Angel Chavez
# Jul 19th, 2025
# Python 3.13.5
# fuel cost estimator based on distance traveled in miles, fuel-efficiency in MPG, and cost of fuel.

print('---- Road Trip Fuel Cost Estimator ----')

# prompts user to input data needed for calculations
total_distance = float(input('Input total distance traveled in miles: '))
fuel_efficiency = float(input('Input fuel-efficiency for your vehicle(MPG): '))
fuel_cost = float(input('Input the current cost of gas per gallon(USD): '))

# formula for total fuel needed and total cost of trip
fuel_needed = total_distance / fuel_efficiency
total_cost = fuel_needed * fuel_cost

# output calculations to the screen
print(f'\nThe amount of fuel you need is {fuel_needed:.2f} gallons')
print(f'The total cost for your trip is ${total_cost:.2f}')