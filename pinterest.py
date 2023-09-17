from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import config

class Scraper:
    def pinterest_scraper(search):
        scroll_num = 1
        sleepTimer = 1
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

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # File.write_file("index.html", driver.page_source)
        find_images(soup)

def rand_proxy():
    proxy = random.choice(config.ips)
    return proxy

def write_file(file_name, page):
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(page.page_source)


def find_images(soup):
    for link in soup.findAll('img'):
        print(link.get('src'))
    for links in soup.findAll('a'):
        print(links.get('href'))


if __name__ == "__main__":
    search = input("Keyworld: ")
    Scraper.pinterest_scraper(search)


