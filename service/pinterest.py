from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class PinterestService:
    def search_parser(search: str, ):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(f"https://pinterest.com/search/pins/?q={search}")  
            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')
            
        return html
    
    def get_links(html):
        div_links = html.select('a[href^="/pin/"]')
        img_links = [div_link.get('href') for div_link in div_links]
        
        return img_links
    
    def link_parser(link):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(link)  
            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')

        return html
    
    def get_img_src(html):
        source = html.select('img[src^="https://i.pinimg.com/564x/"]').get('href') #https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property
        return source



