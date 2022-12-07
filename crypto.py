import requests
import json

url = "https://api.coinmarketcap.com/v1/ticker/"

response = requests.get(url)

data = json.loads(response.text)

for cryptocurrency in data:
    print(cryptocurrency['name'] + ": $" + cryptocurrency['price_usd'])