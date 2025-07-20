# Angel Chavez
# Jul 19th, 2025
# Python 3.13.5
# bank app simulator that displays account info and handles deposits/withdrawals
# refactored once Jul 19 21:45

def display_account(account_holder, account_number, balance):
    """Outputs account info"""

    print('---- Bank Account Simulator ----')
    print(f'\nWelcome {account_holder} Account Number:{account_number}')
    print(f'Your current Balance is: ${balance:.2f}')

def deposit(balance):
    """Adds deposit amount to balance"""

    # get data from user
    deposit = float(input('Enter Deposit Amount: '))

    # add deposit to total balance and then display balance
    balance += deposit
    print('\nDeposit Successful')
    print(f'Your current balance is: ${balance:.2f}')
    return balance

def withdrawal(balance):
    """Subtracts withdrawal amount from balance"""
    # data input from user
    withdrawal = float(input('Enter Withdrawal Amount: '))

    # if-else to check if the withdrawal amount exceeds the current available balance
    # subtracts withdrawal from total balance and then display balance, if not
    if balance < withdrawal:
        print('\n\t***Insuffecient Funds Transaction Canceled***')
    else:
        balance -= withdrawal
        print('\nWithdrawal Successful')
        print(f'Your current balance: ${balance:.2f}')
    return balance

def menu_loop(balance):
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
                balance = deposit(balance)
            elif user_data == '2':
                balance = withdrawal(balance)
            elif user_data == 'q':
                break
            else:
                print('\n\tPLEASE INPUT "1", "2", or "q"')
        except ValueError:
            print('\n\tPlease input a number')

def main():
    """Main function that sets variables and makes calls to functions"""

    # set default values to our variables
    account_number = 100001
    account_holder = 'John Smith'
    balance = 100.0

    display_account(account_holder, account_number, balance)

    menu_loop(balance)

main()