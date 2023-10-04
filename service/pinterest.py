from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from model.image import Image

class PinterestService:
    def search_parser(self, search: str):
        """_summary_

        Args:
            search (str): Pinterest research's keywords or theme (pokemon, anime, plane ...)

        Returns:
            _type_: _description_
        """
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(f"https://pinterest.com/search/pins/?q={search}")  
            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')
            
        return html

    
    def get_links(self, html):
        div_links = html.select('a[href^="/pin/"]') 
        img_links = [div_link.get('href') for div_link in div_links]
        
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
        image_src = html.select_one('img').get('src')

        if "/736x/" in image_src:
            image_src = image_src.replace("/736x/", "/originals/")

        return image_src

    def get_all_img(self, links: list):
        all_img = [self.get_img_src(link) for link in links]
        return all_img
    
    def get_title(self, html):
        title = html.select_one('h1').get_text()
        if title:
            return title
        else:
            return "None"

    def get_user_tag(self, html):
        creator_div = html.find('div', attrs={"data-test-id": "creator-avatar"})
        return creator_div.a['href']
