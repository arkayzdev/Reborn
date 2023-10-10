from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class AreNaService:
    def __init__(self) -> None:
        pass

    def search_parser(self, search: str):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            
            page.goto(f"https://www.are.na/search/{search}/blocks?block_filter=IMAGE")

            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')
            
        return html
    

    def get_links(self, html):
        div_links = html.select('a[href^="/block/"]')
        img_links = [f"https://are.na{div_link.get('href')}" for div_link in div_links]

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
        link = html.select_one('a[href^="https://d2w9rnfcy7mm78.cloudfront.net/"]').get('href')
        title = html.select_one('img').get('title')
        return (link, title)
    

    def get_all_img(self, links: list):
        all_img = [self.get_img_src(link) for link in links]
        return all_img
            
    
