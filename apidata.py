import pandas as pd
import requests

# URL to scrape
url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=API-KEY-HERE"
response = requests.get(url)

df = pd.DataFrame(response.json())
df.to_csv("file_name.csv")
