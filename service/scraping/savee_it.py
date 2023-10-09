from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

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

            connect(page)
            
            page.goto(f"https://savee.it/{search}/")

            page.wait_for_selector("img")  

            search_box = page.locator('input[placeholder="Search new inspiration"]')
            search_box.type(search, delay=100)
            page.wait_for_timeout(2_000)

            html = BeautifulSoup(page.content(), 'html.parser')
            
        return html
    

    def get_link(self, html):
        links = html.select('a[href^="/i/"]')
        img_links = [div_link.get('href') for div_link in links]

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

    def get_img_src(self, html):
        imgs_links = html.select('img')
        return (imgs_links[-1].get('src'), imgs_links[-1].get('alt'))
    
    def get_all_img(self, links: list):
        all_img = [self.get_img_src(link) for link in links]
        return all_img
            
