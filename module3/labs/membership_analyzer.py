# Angel Chavez
# Jul 28th, 2025
# Python 3.13.5
# club membership data analyzer using sets

math_club = {'angel', 'larry', 'lawrence', 'joseph', 'adrian'}
cybersecurity_club = {'larry', 'angel', 'terry', 'andrea', 'addison'}

print(f'Math students: {math_club}')
print(f'Cyber student: {cybersecurity_club}\n')

both_clubs = math_club.intersection(cybersecurity_club)
print(f'Students in BOTH clubs: {both_clubs}\n')

only_math = math_club.difference(cybersecurity_club)
print(f'Students only in the Math club {only_math}\n')

only_cyber = cybersecurity_club.difference(math_club)
print(f'Students only in the Cyber club {only_cyber}\n')

all_students = math_club.union(cybersecurity_club)
print(f'All students in clubs {all_students}')