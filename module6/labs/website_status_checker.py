# Angel Chavez
# Aug 12th, 2025
# Python 3.13.5
# simple script that checks to see if a website is up and running

import requests
import time

urls = [
    'https://google.com',
    'https://resume.it-anc.cloud',
    'https://blog.it-anc.cloud'
]

try:
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'GET Request Success for {url} !')
            time.sleep(2)
        else:
            print('GET request failed with status code: ', response.status_code)
            time.sleep(3)
except Exception as e:
    print(f'Unexpected Error: {e}')

print('All Done!')