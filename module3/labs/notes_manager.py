# Angel Chavez
# Jul 28th, 2025
# Python 3.13.5
# student note manager using python, allows users to read or append to a file called "notes.txt"

print('Welcome to your note manager')

# forever loops through menu until "q" is entered
while True:
    
    # get data from user
    user_choice = input('Would you like to "append" a note or "read" a note?("q" to quit): ')
    
    # appends file based off user_append, with error handling
    if user_choice == 'append':
        user_append = input('Write your note in a single line: ')
        try:
            with open('module3/labs/notes.txt', 'a') as write_file:
                write_file.write(f'{user_append}\n')
        except PermissionError:
            print('Error You Do Not Have Permission For That Action: ')
        except FileNotFoundError:
            print('Error File Not Found: ')
    # reads content of file
    elif user_choice == 'read':
        try:
            with open('module3/labs/notes.txt', 'r') as read_file:
                for line in read_file:
                    print(line.strip())
        except FileNotFoundError:
            print('\tError File Not Found! ')
    # quits loop
    elif user_choice == 'q':
        print('Thank You, Goodbye!')
        break
    # handles unexpected input from user
    else:
        print('Please enter a valid choice')