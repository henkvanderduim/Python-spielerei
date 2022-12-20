# importing necessary libraries
import requests
from bs4 import BeautifulSoup

# getting the website page
url = "https://subslikescript.com/movies"
page = requests.get(url)

# parsing the page
soup = BeautifulSoup(page.content, "html.parser")

# finding the element with tag 'ul' and class 'scripts-list'
scripts_list = soup.find("ul", {"class": "scripts-list"})

# looping through the elements to get the text attribute
for li in scripts_list.find_all("a"):
    print(li.text)
