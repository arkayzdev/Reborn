import requests
from bs4 import BeautifulSoup

res = requests.get('https://pinterest.com/search/pins/?q=gojo')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(res.text)