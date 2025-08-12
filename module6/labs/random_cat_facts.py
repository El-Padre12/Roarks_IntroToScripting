# Angel Chavez
# Aug 12th, 2025
# Python 3.13.5
# script that can deliver fun, random facts about cats using a public 

import requests

def cat_fact_generator():
    """Generates up to 5 random facts about cats based on user input"""

    base_url = 'https://catfact.ninja/facts'

    try:
        user_data = int(input('Enter how many random cat facts you desire(1-5): ').strip())

        url = f'{base_url}?limit={user_data}'

        response = requests.get(url) 
            
        if 1<= user_data <= 5:
            if response.status_code == 200:
                data = response.json()

                for fact in data['data']:
                    print(f' - {fact["fact"]}')
            else:
                print('Failed to retrieve facts.')      
        else:
            print('Please enter a valid input (1-5).')
    except ValueError:
        print('please enter a number')

cat_fact_generator()