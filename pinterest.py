from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
from config import Proxy

class Scraper:
    def pinterest_scraper(search, proxy):
        scroll_num = 1
        sleepTimer = 1
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument(f'--proxy-server={proxy}')
        driver = webdriver.Chrome(options=options)

        url = f'https://pinterest.com/search/pins/?q={search}'
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for i in range (1, scroll_num):
            driver.execute_script("window.scrollTo(1, 1000000)")
            print('scroll-down')
            time.sleep(sleepTimer)
    
        
        for link in soup.findAll('img'):
            print(link.get('src'))
              
        
        # print(driver.page_source)
        print(soup.getText())
        write_file(driver.page_source)
    
     




def write_file(page):
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(page)


if __name__ == "__main__":
    search = input("Keyworld: ")
    Scraper.pinterest_scraper(search, Proxy.get_proxy())



