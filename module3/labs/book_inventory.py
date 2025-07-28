# Angel Chavez
# Jul 28th, 2025
# Python 3.13.5
# book store inventory manager using dictionaries

inventory = {
    'Intro to Python': 8,
    'Data Structures & Algorithms': 25,
    'Web Development': 14,
    'Linear Algebra': 3
}

# output current inventory to the screen
print('Current Inventory\n')
for item, quantity in inventory.items():
    print(f'- {item}: {quantity} in stock')

while True:
    purchased = input('Enter the title of the book you would like to purchase(enter "q" to quit): ')

    # updates inventory based of user input
    # if its not it notifies the user with a warning and then keeps asking until user quits
    if purchased in inventory:
        print(f'\n"{purchased}" purchased successfully')
        inventory[purchased] -= 1
    elif purchased == 'q':
        print('Thank you for shopping goodbye! ')
        break
    else:
        print(f'\nThat book "{purchased}" does not seem to be in our inventory')
        print('Ensure you typed the title correctly(case-sensitive)')

    print('\nUpdated Inventory\n')
    for item, quantity in inventory.items():
        print(f'- {item}: {quantity} in stock')