import requests


r = requests.get("https://www.henkvanderduim.nl")
print(r.status_code)
print(r.ok)
