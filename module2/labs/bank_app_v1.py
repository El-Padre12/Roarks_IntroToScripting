# Angel Chavez
# Jul 19th, 2025
# Python 3.13.5
# bank app simulator that displays account info and handles deposits/withdrawals

# set default values to our variables
account_number = 100001
acount_holder = 'John Smith'
balance = 100.0

# output info before main menu loop
print('---- Bank Account Simulator ----')
print(f'\nWelcome {acount_holder}:{account_number}.')
print(f'Your current Balance is: ${balance:.2f}')

# indefinite loop until 'q' is inputed by the user
while True:
    # tries block of code with a ValueError exception for error handling
    try:
        print('\n---- Menu Selection ----')
        print('1. deposit')
        print('2. withdrawal')

        # prompt user for data
        user_data = input('Make Selection(type "q" to exit): ')

        # if-elif-if logic responds to user_data input
        if user_data == '1':
            deposit = float(input('Enter Deposit Amount: '))

            balance += deposit
            print('\nDeposit Successful')
            print(f'Your current balance is: ${balance:.2f}')
        elif user_data == '2':
            withdrawal = float(input('Enter Withdrawal Amount: '))

            # nested if-else to check if the withdrawal amount exceeds the current available balance
            if balance < withdrawal:
                print('\n\t***Insuffecient Funds Transaction Canceled***')
            else:
                balance -= withdrawal
                print('\nWithdrawal Successful')
                print(f'Your current balance: ${balance:.2f}')
                
        elif user_data == 'q':
            break
        else:
            print('\n\tPLEASE INPUT "1", "2", or "q"')
    except ValueError:
        print('\n\tPlease input a number')