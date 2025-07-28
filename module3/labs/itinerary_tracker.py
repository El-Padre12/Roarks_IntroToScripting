# Angel Chavez
# Jul 28th, 2025
# Python 3.13.5
# travel itinerary tracker using tuples

trip1 = ('Tokyo', 5, 'Train')
trip2 = ('L.A.', 3, 'Plane')
trip3 = ('Germany', 15, 'Ship')

itinerary = [trip1, trip2, trip3]

print('Here are your planned trips: \n')
for i, (city,days,mode) in enumerate(itinerary, start=1):
    print(f'{i} {city} - {days} days by {mode}')

trip_details = input('\nEnter the number of the trip you want details for(1-3): ')

if trip_details == '1':
    print(f'Destination: {trip1[0]}')
    print(f'Days: {trip1[1]}')
    print(f'Transportation: {trip1[2]}')
elif trip_details == '2':
    print(f'Destination: {trip2[0]}')
    print(f'Days: {trip2[1]}')
    print(f'Transportation: {trip2[2]}')
elif trip_details == '3':
    print(f'Destination: {trip3[0]}')
    print(f'Days: {trip3[1]}')
    print(f'Transportation: {trip3[2]}')
else:
    print('Please enter a valid response')