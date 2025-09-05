# Angel Chavez
# Sept 4th, 2025
# Python 3.13.5
# simple game inventory viewer program

import csv

try:
    with open('module3/labs/inventory.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)    # skip the header

        print('Welcome to your game inventory')
        # make the output look like a table
        print(f'{"Item":<15} | {"Category":<8} | {"Qty":<3} | {"Rarity":<8}')
        print('-' * 43)

        for row in reader:
            item = row[0]
            category = row[1]
            quantity = row[2]
            rarity = row[3]
            
            print(f'{item:<15} | {category:<8} | {quantity:<3} | {rarity:<8}')
        
except FileNotFoundError:
    print('the file was not found')