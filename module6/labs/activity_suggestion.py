# Angel Chavez
# Aug 12th, 2025
# Python 3.13.5
# script tool that helps users discover new activities when they feel bored

import requests
import pprint

def activity_generator():
    

    base_url = 'https://bored-api.appbrewery.com/'

    user_data = input('Enter activity type: ')

    url = f'{base_url}filter?type={user_data}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # data returns a list of dicts so we loop over it directly calling to the indexes
        for index in data:
            print(f' - {index["activity"]} ({index["participants"]} participants)')
    else:
        print('no activities found')

def main():
    activity_generator()

main()