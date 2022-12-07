# Import necessary modules
import requests
from bs4 import BeautifulSoup

# Function to get the current exchange rate for a given currency
def get_exchange_rate(currency):
    # Request exchange rate data from website
    response = requests.get('https://www.exchangerate-api.com/' + currency + '/USD')
    # Parse HTML data
    soup = BeautifulSoup(response.text, 'html.parser')
    # Get the exchange rate
    exchange_rate = soup.find('div', {'class': 'rate'}).get_text()
    return float(exchange_rate)

# Function to convert a given amount of a currency to USD
def convert_to_usd(amount, currency):
    # Get the exchange rate
    exchange_rate = get_exchange_rate(currency)
    # Convert the amount to USD
    converted_amount = amount * exchange_rate
    return converted_amount

# Prompt the user for the amount and currency to convert
amount = float(input('Enter the amount to convert: '))
currency = input('Enter the currency to convert (e.g. EUR): ')

# Convert the amount to USD and print the result
converted_amount = convert_to_usd(amount, currency)
print('The converted amount is: $' + str(converted_amount))