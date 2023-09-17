from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import config

scroll_num = 1
sleepTimer = 1

def rand_proxy():
    proxy = random.choice(config.ips)
    return proxy


def pinterest_scraper(search):
    url = f'https://pinterest.com/search/pins/?q={search}'
    options = webdriver.ChromeOptions()
    proxy = rand_proxy()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f'--proxy-server={proxy}')
    # driver = webdriver.Chrome(executable_path='chromedriver.exe', options= options)
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    for i in range (1, scroll_num):
        driver.execute_script("window.scrollTo(1, 1000000)")
        print('scroll-down')
        time.sleep(sleepTimer)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for link in soup.findAll('img'):
        print(link.get('src'))


pinterest_scraper('gojo')


