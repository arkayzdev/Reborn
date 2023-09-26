import requests
from bs4 import BeautifulSoup
import random

class Proxy:
    def get_proxy():
        url = f'https://free-proxy-list.net/'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        ips = soup.select('tbody > tr')[:-9]

        available_ips = []

        for idx, row in enumerate(ips):
            https = row.select_one('.hx').text
            if https == 'yes':
                available_ips.append({
                    'ip': row.select_one('td:nth-of-type(1)').text,
                    'port': row.select_one('td:nth-of-type(2)').text
                })
         
        proxy = random.choice(available_ips)
        return f"{proxy['ip']}:{proxy['port']}"
   


       



