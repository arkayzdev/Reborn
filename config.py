import requests
from bs4 import BeautifulSoup
import pprint

url = f'https://free-proxy-list.net/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

ips = soup.findAll('tr')

available_ips = []

for idx, ip in enumerate (ips):
    https = ip.select('.hx')[0].getText()
    if https == 'yes':
        # print(len(ip))
        for column, value in enumerate (ip):
            print(value)
            available_ips.append('ip': value[0])
        break



