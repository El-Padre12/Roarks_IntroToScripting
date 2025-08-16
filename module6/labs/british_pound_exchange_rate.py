# Angel Chavez
# Aug 15th, 2025
# Python 3.13.5
# script tool that display exchange rates from GBP to other currencies (like USD, EUR, JPY, etc.) so users can see how much their pounds are-     # worth in other countries.

from bs4 import BeautifulSoup
import requests

url = 'https://www.x-rates.com/table/?from=GBP&amount=1'
response = requests.get(url)

response.encoding = 'utf-8'
html = response.text

if response.status_code == 200:
    soup = BeautifulSoup(html, 'html.parser')

    # finds the first table with the class 'ratesTable'
    table = soup.find('table', class_='ratesTable')

    if table:
        rows = table.find_all('tr')[1:]     # skip header row
        print('Top 5 GBP Exhcange Rates')
        print('-' * 30)
        # loop over the first 5 rows
        for row in rows[:5]:
            cols = row.find_all('td')
            if len(cols) >= 2:
                currency = cols[0].get_text(strip=True)     # gets currency name
                rate = cols[1].get_text(strip=True)         # gets EX rate
                # formated
                print(f'{currency:<17} | {float(rate):.3f}') 
        print('-' * 30)
    else:
        print('Exhange rates table not found on page.')
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
