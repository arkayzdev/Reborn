from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from model.image import Image
import threading
import queue

class SaveeItService:
    def __init__(self) -> None:
        pass

    def connect(self, page):
        page.goto(f"https://savee.it/login/")  
        page.wait_for_selector("input")  

        #Login ArkayzScrape:Scrape456951
        username_box = page.locator('input[name="usernameOrEmail"]')
        username_box.type("ArkayzScrape", delay=100)
        
        password_box = page.locator('input[name="password"]')
        password_box.type("Scrape456951", delay=100)

        confirm_button = page.locator('button[type="submit"]')
        confirm_button.click()

        page.wait_for_timeout(2_000)
        


    def search_parser(self, search: str):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()

            self.connect(page)
            
            page.goto(f"https://savee.it/search/?q={search}")

            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')
            
        return html
    

    def get_links(self, html):
        links = html.select('a[href^="/i/"]')
        img_links = [f"https://savee.it{div_link.get('href')}" for div_link in links]

        return img_links
    

    def link_parser(self, link: str):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(link)  
            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')

        return html

    def get_img_info(self, html):
        imgs_links = html.select('img')

        image_src = imgs_links[-1].get('src')
        alt = imgs_links[-1].get('alt')

        return {'source': image_src, 'alt': alt} 
    

    def get_all_img(self, links: list):
        all_img = []
        for link in links:
            html = self.link_parser(link)
            img_info = self.get_img_info(html)
            all_img.append(Image(img_info['alt'], link, img_info['source'], 'Savee', 'None', img_info['alt']))
        return all_img
            