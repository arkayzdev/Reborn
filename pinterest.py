from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
from config import Proxy

class Scraper:
    def pinterest_scraper(search):
        scroll_num = 1
        sleepTimer = 1
        url = f'https://pinterest.com/search/pins/?q={search}'
        options = webdriver.ChromeOptions()
        proxy = Proxy.get_proxy()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument(f'--proxy-server={proxy}')
        driver = webdriver.Chrome(options=options)
        # driver.set_page_load_timeout(60)
        # try:
        driver.get(url)
        # print("URL successfully Accessed")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
     
        # except TimeoutException:
        #     print("Page load Timeout Occured. Quiting !!!")
        #     driver.quit()
            
            

        for i in range (1, scroll_num):
            driver.execute_script("window.scrollTo(1, 1000000)")
            print('scroll-down')
            time.sleep(sleepTimer)

        
        print(soup.find('title').getText())
        print(soup.getText())
        write_file(driver.page_source)
        find_images(soup)




def write_file(page):
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(page)


def find_images(soup):
    for link in soup.findAll('img'):
        print(link.get('src'))


if __name__ == "__main__":
    search = input("Keyworld: ")
    Scraper.pinterest_scraper(search)



