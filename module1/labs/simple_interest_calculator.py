# Angel Chavez
# Jul 17th, 2025
# Python 3.13.5
# simple interest yeild calculator for an investment or savings account

# takes input from user as a float an stores in appropriately names variables
print('---- Simple Interest Calculator ----\n')
principal_amount = float(input('Input principal investment amount in USD: '))
annual_interest_rate = float(input('Input the anual interest rate as a percentage: '))
time = float(input('Input how long you will hold this investment in years: '))

# formula given to me for simple interest
interest_yeild = (principal_amount * annual_interest_rate * time) / 100

# out put of calculations to the screen
print(f'\nA ${principal_amount:.2f} investment at a {annual_interest_rate:.2f}% interest rate, for {time} years ')
print(f'has a yeild of ${interest_yeild:.2f}')