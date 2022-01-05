import math
import sys
import os

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hallo, {}".format(who_to_greet)
    return greeting


r = requests.get("https://henkvanderduim.nl")
print(r.status_code)
