# Angel Chavez
# Jul 22nd, 2025
# Python 3.13.5
# course schedule manager using a list.

schedule = []
users_choice = ''

print(f'---- Welcome to the Course Planner ----')
schedule.append(input('Enter a course: '))
schedule.append(input('Enter a course: '))
schedule.append(input('Enter a course: '))

print('\nYour current schedule: ')

for course in schedule:
    print(f'- {course}')

users_choice = input('\nWould you like to drop a course?(yes/no): ')

if users_choice == 'yes':
    course = input('Enter course name you want dropped: ')
    if course in schedule:
        schedule.remove(course)
    else:
        print('Could not find course')
elif users_choice == 'no':
    print('Okay see yall next time ')
else:
    print('Please enter a valid response')

print('\nYour up to date schedule: ')

for course in schedule:
    print(f'- {course}')
 
print(f'You are registered in {len(schedule)} classes')